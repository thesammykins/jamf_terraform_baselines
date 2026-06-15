# TECH.md — NIST mSCP → Jamf Pro Terraform Modules

## Architecture Overview

```
┌──────────────────────────────────────────────────────────┐
│                    GitHub Actions CI                      │
│                                                          │
│  ┌──────────────┐   ┌──────────────┐   ┌─────────────┐  │
│  │ mSCP Release │   │  Foundation  │   │  Exemption  │  │
│  │    Poller    │   │   Updater    │   │  Validator  │  │
│  └──────┬───────┘   └──────┬───────┘   └──────┬──────┘  │
│         │                  │                  │         │
│         ▼                  ▼                  ▼         │
│  ┌──────────────────────────────────────────────────┐   │
│  │              Code Generator (Python)              │   │
│  │  • Reads mSCP rule YAML from cloned repo         │   │
│  │  • Maps rules → jamfplatform_cbengine_benchmark  │   │
│  │  • Generates Terraform HCL modules               │   │
│  │  • Generates exemption tracking outputs           │   │
│  └──────────────────────┬───────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌──────────────────────────────────────────────────┐   │
│  │           Terraform Validate + Plan               │   │
│  └──────────────────────┬───────────────────────────┘   │
│                         │                                │
│                         ▼                                │
│  ┌──────────────────────────────────────────────────┐   │
│  │                 Open PR                           │   │
│  │  • Changed files diff                             │   │
│  │  • terraform plan output                          │   │
│  │  • Rule-level changelog                           │   │
│  │  • Exemption status report                        │   │
│  └──────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

## Variant A — Compliance Baseline Generation

### Data flow

```
usnistgov/macos_security (git clone at tag)
  ├── baselines/*.yaml          → which rules belong to each baseline
  ├── rules/{audit,auth,os,etc}/*.yaml  → per-rule check/fix/result/metadata
  ├── VERSION.yaml              → current mSCP version info
  └── includes/mscp-data.yaml   → ODV defaults, shared data
                                  │
                                  ▼
              Code generator (scripts/generate_tf_compliance.py)
                                  │
                                  ▼
              modules/compliance/{baseline}/macos_{version}/
                ├── main.tf              → benchmark resource + device group
                ├── variables.tf         → enforcement_mode, exemptions, overrides
                ├── outputs.tf           → benchmark ID, exemption report
                └── README.md            → baseline description, rule count, CCE refs
```

### Generator logic

The generator (`scripts/generate_tf_compliance.py`) runs inside the mSCP container or against a local clone:

1. **Parse VERSION.yaml** for current branch + revision
2. **For each baseline YAML** in `baselines/`:
   - Extract `profile[].section` and `profile[].rules[]`
   - Cross-reference each rule ID against its rule YAML file for:
     - `title`, `discussion`
     - `references.nist.cce` (per macOS version)
     - `references.nist.800-53r5` (control mappings)
     - `references.disa.disa_stig` (STIG ID)
     - `severity`
     - `platforms.macOS` version-specific `enforcement_info`
   - Group rules by section (audit, auth, icloud, os, pwpolicy, system_settings, supplemental, inherent)
3. **Generate one Terraform module per baseline × macOS version**
4. **For each module:**
   - Generate `jamfplatform_device_group` with OS version criteria
   - Generate `data.jamfplatform_cbengine_rules` referencing the baseline
   - Generate `jamfplatform_cbengine_benchmark` with:
     - Pinned source branch + revision
     - All rules from the baseline, default-enabled
     - Rule descriptions pulled from rule YAML `discussion` field
   - Generate variables for `rule_overrides`, `disabled_rules`, `exemptions`

### Generated Terraform resource shape

Each compliance module produces approximately:

```hcl
# modules/compliance/cis_lvl1/macos_26/main.tf

locals {
  all_rules = [
    { id = "os_gatekeeper_enable", title = "Enable Gatekeeper", severity = "high" },
    { id = "os_sip_enable", title = "Enable System Integrity Protection", severity = "high" },
    # ... all rules for this baseline
  ]

  enabled_rules = {
    for rule in local.all_rules :
    rule.id => rule
    if !contains(var.disabled_rules, rule.id) && !contains(keys(var.exemptions), rule.id)
  }
}

resource "jamfplatform_device_group" "this" {
  name        = "${var.baseline_display_name} — macOS ${var.macos_version}"
  group_type  = "smart"
  device_type = "computer"
  criteria = [{
    criteria = "Operating System Version"
    operator = "greater than or equal"
    value    = var.macos_version_min
  }]
}

data "jamfplatform_cbengine_rules" "this" {
  baseline_id = var.baseline_id
}

resource "jamfplatform_cbengine_benchmark" "this" {
  title              = var.baseline_display_name
  description        = "${var.baseline_display_name} — mSCP ${var.mscp_branch} @ ${var.mscp_revision} — Managed by Terraform"
  source_baseline_id = var.baseline_id

  sources = [for s in data.jamfplatform_cbengine_rules.this.sources : {
    branch   = s.branch
    revision = s.revision
  }]

  rules = [
    for r in data.jamfplatform_cbengine_rules.this.rules : {
      id      = r.id
      enabled = contains(keys(local.enabled_rules), r.id)
      odv_value = try(var.rule_overrides[r.id].odv_value, null)
    }
  ]

  target_device_group = jamfplatform_device_group.this.id
  enforcement_mode    = var.enforcement_mode
}
```

### Exemption processing in Terraform

Exemptions are processed through Terraform locals:

```hcl
# modules/compliance/_shared/exemptions.tf

locals {
  exemption_report = {
    for k, v in var.exemptions : k => merge(v, {
      module        = var.baseline_id
      macos_version = var.macos_version
      timestamp     = timestamp()
    })
  }

  has_expired_exemptions = anytrue([
    for e in local.exemption_report :
    can(e.expires) ? timecmp(e.expires, timestamp()) < 0 : false
  ])

  # Precondition: no expired exemptions in apply
  # (CI also validates this at PR time via a script)
}

resource "terraform_data" "exemption_report" {
  count = length(local.exemption_report) > 0 ? 1 : 0

  input = local.exemption_report
}

output "exemptions" {
  value       = local.exemption_report
  description = "Active exemptions with audit justification"
}
```

### Per-PR changelog generation

```
scripts/generate_changelog.py
  • Reads previous module state from committed files (git show HEAD^{tree})
  • Compares rule lists: ADDED, REMOVED, MODIFIED
  • Outputs markdown table for PR body
```

Example output:

```markdown
## Rule Changes — CIS Level 1 (macOS 26) — tahoe_rev1 → tahoe_rev2

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | os_loginwindow_adminhostinfo_disabled | Disable AdminHostInfo at Login Window |
| ADDED | os_safari_clear_history_disable | Disable Safari Clear History |
| MODIFIED | pwpolicy_account_lockout_enforce | Account Lockout Enforcement (updated check logic) |
| MODIFIED | system_settings_screensaver_password_enforce | Screensaver Password (additional remediation) |
| REMOVED | system_settings_software_update_enforce | (replaced by per-setting rules) |
```

---

## Variant B — macAdmin Foundation

### Architecture

Variant B modules are **hand-authored** (not generated) because they embed operational judgment rather than compliance rule mapping. They are updated via periodic PRs when:
- PPPC bundle identifiers change (app updates)
- Community best practices shift
- New Jamf Pro provider features become available
- Apple introduces new configuration domains in macOS updates

### Foundation module pattern

Each foundation module follows a consistent pattern:

```hcl
# modules/foundation/security-baseline/main.tf

resource "jamfpro_macos_configuration_profile_plist" "filevault" {
  count = var.enable_security_baseline ? 1 : 0

  name                = "Security Baseline — FileVault"
  description         = "Enforces FileVault full-disk encryption. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads            = templatefile("${path.module}/templates/filevault.mobileconfig.tftpl", {})
  payload_validate    = true

  scope {
    all_computers = true
    all_jss_users = false
  }
}
```

PLIST payloads are stored as `.mobileconfig.tftpl` templates in a `templates/` subdirectory, not as generated strings, so they're readable and reviewable.

### Foundation exemption at the module level

```hcl
variable "exemptions" {
  type = map(object({
    reason                = string
    ticket                = optional(string)
    risk_status           = string
    compensating_controls = optional(string)
    reviewer              = optional(string)
    review_date           = optional(string)
    expires               = optional(string)
  }))
  default     = {}
}

# Each resource guards itself
resource "jamfpro_macos_configuration_profile_plist" "filevault" {
  count = (
    var.enable_security_baseline &&
    !contains(keys(var.exemptions), "filevault")
  ) ? 1 : 0
  # ...
}
```

---

## CI Pipeline Design

### Workflow: `compliance-update.yml`

```yaml
name: Compliance Baseline Update

on:
  schedule:
    - cron: '0 6 * * 1'           # Weekly Monday 06:00 UTC
  workflow_dispatch:
    inputs:
      mscp_branch:
        description: 'mSCP branch to process'
        required: false
        default: 'all'

jobs:
  detect-releases:
    runs-on: ubuntu-latest
    outputs:
      branches: ${{ steps.detect.outputs.branches }}
    steps:
      - id: detect
        run: |
          # Poll GitHub releases API for new tags since last recorded revision
          python scripts/detect_mscp_releases.py \
            --state-file .ci/mscp-revision-state.json \
            --output new-releases.json

  generate:
    needs: detect-releases
    if: needs.detect-releases.outputs.branches != '[]'
    strategy:
      matrix:
        branch: ${{ fromJSON(needs.detect-releases.outputs.branches) }}
    runs-on: ubuntu-latest
    container: ghcr.io/usnistgov/mscp_2.0:latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.head_ref }}

      - name: Clone mSCP at release tag
        run: |
          git clone -b ${{ matrix.branch }} https://github.com/usnistgov/macos_security.git /tmp/mscp
          cd /tmp/mscp
          git checkout ${{ steps.detect.outputs[format('{0}_tag', matrix.branch)] }}

      - name: Generate compliance modules
        run: |
          python scripts/generate_tf_compliance.py \
            --mscp-path /tmp/mscp \
            --output modules/compliance \
            --branch ${{ matrix.branch }}

      - name: Generate changelog
        run: |
          python scripts/generate_changelog.py \
            --mscp-path /tmp/mscp \
            --branch ${{ matrix.branch }} \
            --output changelog.md

      - name: Terraform validate
        run: |
          for dir in modules/compliance/*/macos_*/; do
            (cd "$dir" && terraform init -backend=false && terraform validate)
          done

      - name: Create pull request
        uses: peter-evans/create-pull-request@v7
        with:
          title: "compliance: ${{ matrix.branch }} baseline update"
          body-path: changelog.md
          branch: "auto/compliance-${{ matrix.branch }}"
          labels: "compliance,automated"
```

### Workflow: `exemption-check.yml`

```yaml
name: Exemption Validation

on: [push, pull_request]

jobs:
  check-exemptions:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for expired exemptions
        run: |
          python scripts/check_exemptions.py \
            --modules-dir modules/ \
            --enforce-expiry true

      - name: Check exemption completeness
        run: |
          python scripts/check_exemptions.py \
            --modules-dir modules/ \
            --require-ticket true \
            --warn-missing-reviewer true
```

### Exemption check script logic

```python
# scripts/check_exemptions.py — pseudocode
for each module:
    parse variables.tf for exemption blocks
    for each exemption:
        if expires < today():
            if enforce_expiry:
                fail(f"EXPIRED: {rule_id} in {module_name} expired {expires}")
        if require_ticket and not ticket:
            warn(f"MISSING TICKET: {rule_id} in {module_name}")
        if warn_missing_reviewer and not reviewer:
            warn(f"MISSING REVIEWER: {rule_id} in {module_name}")
```

---

## Repository Structure (Complete)

```
jamf_mscp_tf/
├── .github/
│   └── workflows/
│       ├── compliance-update.yml
│       ├── foundation-update.yml
│       └── exemption-check.yml
├── .ci/
│   └── mscp-revision-state.json      # Tracks last-seen revision per branch
├── modules/
│   ├── compliance/
│   │   ├── _shared/
│   │   │   └── exemptions.tf          # Shared exemption processing locals
│   │   ├── 800-53r5_high/
│   │   │   ├── macos_14/
│   │   │   │   ├── main.tf
│   │   │   │   ├── variables.tf
│   │   │   │   ├── outputs.tf
│   │   │   │   └── README.md
│   │   │   ├── macos_15/  (same structure)
│   │   │   └── macos_26/  (same structure)
│   │   ├── cis_lvl1/
│   │   │   └── ...
│   │   └── ... (all 16 baselines)
│   │
│   └── foundation/
│       ├── _shared/
│       │   └── exemptions.tf
│       ├── categories/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── outputs.tf
│       ├── os-version-smart-groups/
│       │   └── ...
│       ├── security-baseline/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   ├── outputs.tf
│       │   └── templates/
│       │       ├── filevault.mobileconfig.tftpl
│       │       ├── firewall.mobileconfig.tftpl
│       │       ├── screensaver.mobileconfig.tftpl
│       │       └── gatekeeper.mobileconfig.tftpl
│       ├── software-updates/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── templates/
│       │       └── software-update.mobileconfig.tftpl
│       ├── pppc-screen-capture/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── pppc-bundle-ids.yaml
│       ├── pppc-accessibility/
│       │   ├── main.tf
│       │   ├── variables.tf
│       │   └── pppc-bundle-ids.yaml
│       ├── device-enrollment/
│       │   ├── main.tf
│       │   └── variables.tf
│       └── inventory-settings/
│           ├── main.tf
│           └── variables.tf
├── scripts/
│   ├── generate_tf_compliance.py      # Variant A code generator
│   ├── generate_changelog.py          # Rule-level changelog
│   ├── detect_mscp_releases.py        # Polls GitHub releases API
│   ├── check_exemptions.py            # Exemption validation
│   └── update_pppc_bundle_ids.py      # PPPC bundle ID updater
├── examples/
│   ├── compliance-only/               # Example using only Variant A
│   │   └── main.tf
│   ├── foundation-only/               # Example using only Variant B
│   │   └── main.tf
│   └── full-stack/                    # Example using both
│       └── main.tf
├── specs/
│   └── mscp-terraform-pipeline/
│       ├── PRODUCT.md
│       └── TECH.md
├── .gitignore
├── .terraform-version
└── README.md
```

---

## Testing Strategy

### Unit tests (Python generator)

- `tests/test_generate_compliance.py`: Verify generator produces valid HCL for each baseline
- `tests/test_changelog.py`: Verify changelog correctly computes ADDED/REMOVED/MODIFIED
- `tests/test_exemptions.py`: Verify exemption check script catches expired/missing fields

### Terraform validation (CI)

- `terraform validate` runs on every generated module in CI
- `terraform fmt -check -recursive` enforces consistent formatting

### Integration tests

- Against a real Jamf Pro staging instance with Jamf Platform API access:
  - Apply one compliance module (CIS L1, macOS 26)
  - Verify benchmark appears in Jamf Pro UI
  - Verify device group has correct criteria
  - Apply with exemptions, verify excluded rules are absent
  - Destroy and verify cleanup

### PPPC bundle ID tests

- `update_pppc_bundle_ids.py` validates bundle IDs against known Apple Bundle ID format
- Test that each supported tool's bundle ID is present and well-formed

---

## Key Design Decisions

1. **Compliance Benchmark Engine over mobileconfig generation**: Jamf's native engine handles rule evaluation, update cadence, and reporting — we don't need to reimplement that. The generated Terraform only needs to declare what to monitor/enforce.

2. **One module per baseline × OS version**: No monolithic module. This avoids coupling — a change to CIS L1 doesn't affect DISA STIG. Consumers include only what they need.

3. **Exemptions as Terraform variables, not comments**: Exemptions are machine-readable, CI-enforceable, and appear in `terraform plan`. A comment in a config file is invisible to automation.

4. **Foundation modules hand-authored, not generated**: These embed operational judgment (which PPPC tools to include, sensible deferral windows). They change slowly and benefit from human curation.

5. **Python for generation, not shell**: The mSCP repository is YAML-heavy. Python's YAML + Jinja2 stack is the right tool for mapping structured rule data to HCL templates.

6. **mSCP 1.0 branches initially, with 2.0 support planned**: The `dev_2.0` branch will become the canonical source once it reaches production. The generator uses the same branch-per-version model as mSCP 1.0 today, with a migration path to the unified 2.0 format when ready.

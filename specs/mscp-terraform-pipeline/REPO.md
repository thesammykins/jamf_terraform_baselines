# REPO.md — Skills, Governance, and Agent Configuration

This spec defines the non-code scaffolding needed after the baseline modules are built: localized skills for agents working in this repo, repository governance files, and the AGENTS.md configuration that tells OpenCode how to operate here.

---

## Skills

Skills live in `.agents/skills/` and provide specialized guidance to agents (human or AI) performing specific tasks in this repository. Each skill is a `SKILL.md` with a name, description, and structured instructions.

### Skill 1: `compliance-baseline-usage`

**Name**: `compliance-baseline-usage`
**Trigger**: "compliance baseline", "mSCP benchmark", "deploy CIS", "deploy STIG", "NIST 800-53 module"
**Purpose**: Guide operators through selecting, configuring, and deploying Variant A compliance modules.

**Contents**:

```markdown
# Compliance Baseline Usage

Deploy NIST mSCP compliance baselines via Jamf Platform Compliance Benchmark Engine.

## PHASE 0: Pre-flight

Verify Jamf Platform API access:
- `JAMFPLATFORM_CLIENT_ID` and `JAMFPLATFORM_CLIENT_SECRET` are set
- Region is correct (`JAMFPLATFORM_BASE_URL` = `https://{us,eu,apac}.apigw.jamf.com`)

## PHASE 1: Select baselines

1. Browse `modules/compliance/` to see available baselines
2. Each baseline has subdirectories per macOS version (`macos_14`, `macos_15`, `macos_26`)
3. Module source path: `./modules/compliance/{baseline_key}/macos_{version}`

Example: NIST 800-53 Moderate for macOS Tahoe:
```hcl
module "nist_80053_moderate_tahoe" {
  source = "./modules/compliance/800-53r5_moderate/macos_26"
}
```

## PHASE 2: Choose enforcement mode

| Mode | Behavior |
|---|---|
| `MONITOR` | Report compliance only, no remediation |
| `MONITOR_AND_ENFORCE` | Remediate non-compliant settings automatically |

Start with `MONITOR` on first deploy. Switch to `MONITOR_AND_ENFORCE` after reviewing the compliance report.

## PHASE 3: Handle exemptions

Rules that conflict with operational needs must be exempted with justification:

```hcl
exemptions = {
  "os_dictation_disable" = {
    reason      = "Clinical staff require dictation"
    ticket      = "SEC-4521"
    risk_status = "ACCEPTED"
  }
}
```

Valid `risk_status` values: `ACCEPTED`, `TEMPORARY`, `ACCEPTED_WITH_COMPENSATING_CONTROLS`, `UNDER_REVIEW`

For `TEMPORARY` exemptions, always set `expires`. CI will block expired exemptions.

## PHASE 4: Apply

```bash
terraform init
terraform plan    # Review exemptions output and resource count
terraform apply -parallelism=1
```

## PHASE 5: Verify

1. Open Jamf Pro → Compliance → Benchmarks
2. Confirm benchmark appears with correct rule count
3. Check device group membership under Inventory → Device Groups
4. Wait for devices to report compliance status

## Common patterns

### Multiple baselines per device group

```hcl
module "cis_l1" {
  source = "./modules/compliance/cis_lvl1/macos_26"
  enforcement_mode = "MONITOR_AND_ENFORCE"
}

module "disa_stig" {
  source = "./modules/compliance/disa_stig/macos_26"
  enforcement_mode = "MONITOR"  # Staggered rollout
  exemptions = {
    # DISA STIG rules that conflict with org policy
  }
}
```

### Per-OS-version targeting

Different baselines for different OS versions:
```hcl
# Enforce CIS L1 on current OS, monitor old OS
module "cis_l1_tahoe"    { source = "./modules/compliance/cis_lvl1/macos_26" }
module "cis_l1_sequoia"  { source = "./modules/compliance/cis_lvl1/macos_15" }
module "cis_l1_sonoma"   { source = "./modules/compliance/cis_lvl1/macos_14" }
```

## Anti-patterns

1. **Skipping MONITOR phase**: Always monitor first, enforce after review.
2. **Empty exemptions**: Never set `reason = ""` or `ticket = ""`. CI will warn.
3. **Deleting modules instead of exempting**: Removing a module source block is invisible to audit. Use exemptions.
4. **Applying to all OS versions without testing**: Test on oldest supported OS first (newer OS may have stricter enforcement).
```

---

### Skill 2: `foundation-setup`

**Name**: `foundation-setup`
**Trigger**: "new Jamf tenant", "Jamf foundation", "macAdmin setup", "Jamf scaffolding", "day zero Jamf"
**Purpose**: Guide operators through deploying the macAdmin Foundation modules for a new Jamf Pro tenant.

**Contents**:

```markdown
# macAdmin Foundation Setup

Deploy standard Jamf Pro scaffolding for new tenants.

## PHASE 0: Pre-flight

Verify Jamf Pro API access:
- `jamfpro_client_id` and `jamfpro_client_secret` are set
- `jamfpro_instance_fqdn` points to the correct instance

## PHASE 1: Inventory current state

```hcl
module "foundation" {
  source = "./modules/foundation"
  
  enable_categories              = true
  enable_os_version_smart_groups = true
  enable_security_baseline       = true
  enable_software_updates        = true
  enable_pppc_screen_capture     = true
  enable_pppc_accessibility      = true
  enable_device_enrollment       = true
  enable_inventory_settings      = true
}
```

## PHASE 2: Module-by-module guidance

### categories
Creates: `Security`, `Productivity`, `Utilities`, `Communication`, `Browsers`, `Developer Tools`
- Safe to run on existing tenants; creates only if absent.
- Used by policies and profiles for organization.

### os-version-smart-groups
Creates smart groups: macOS 14/15/26 + "Unsupported"
- Criterion: `Operating System Version >= X.0`
- Used by compliance benchmarks and scoping.

### security-baseline
Deploys: FileVault, firewall (stealth), screensaver (5 min + password), Gatekeeper, auto-login disable
- All profiles are System-level, non-removable.
- FileVault requires user interaction (password on next login); profile deploys silently.

### software-updates
Deploys: Auto-download, auto-install security updates, defer major 90d, defer minor 14d, RSR enabled
- Adjust `software_update_major_deferral_days` for your testing window.
- RSR rollback is disabled by default (set `rapid_security_response_rollback = false`).

### pppc-screen-capture / pppc-accessibility
Deploys PPPC profiles for common collaboration tools.
- Bundle IDs are sourced from `pppc-bundle-ids.yaml`.
- Default tools: Zoom, Slack, Microsoft Teams, Google Chrome, Webex.
- Set `pppc_tools` to your org's approved list.

### device-enrollment
Configures ADE (Automated Device Enrollment) PreStage.
- Skips: Apple ID, Siri, Touch ID, Screen Time, Privacy, iCloud storage, FileVault, Display Tone, True Tone, Appearance.
- Requires ADE token already configured in Jamf Pro.
- If ADE token isn't provisioned yet, exempt this module.

### inventory-settings
Configures: Computer check-in frequency, software update collection, extension attributes.
- Defaults: check-in every 15 min, software update collection enabled.

## PHASE 3: Apply

```bash
terraform init
terraform plan
terraform apply -parallelism=1
```

## PHASE 4: Post-deploy checks

1. Verify categories appear in Jamf Pro → Settings → Global → Categories
2. Verify smart groups populate in Inventory → Smart Computer Groups
3. Verify profiles deploy in Computers → Configuration Profiles
4. On a test Mac, verify FileVault prompt, screensaver locks, and PPPC allows screen capture for listed tools
5. Enroll a test Mac via ADE; verify setup panes are skipped and MDM profile is non-removable

## Anti-patterns

1. **Enabling device-enrollment without ADE token**: Profile deploys but no devices can enroll.
2. **Skipping PPPC profiles**: Screen capture and accessibility will silently fail for listed tools.
3. **Not adjusting deferral windows**: 90-day major deferral may be too aggressive for some orgs.
```

---

### Skill 3: `manage-exemptions`

**Name**: `manage-exemptions`
**Trigger**: "exemption", "exclude rule", "waive control", "risk acceptance", "compensating control"
**Purpose**: Guide operators through declaring, reviewing, and maintaining exemptions across both variants.

**Contents**:

```markdown
# Managing Exemptions

Declare and track security control exemptions with audit trails.

## When to exempt

Exempt a rule when:
- It conflicts with a documented operational requirement
- It is incompatible with required software or hardware
- You have compensating controls that provide equivalent protection
- It will be enabled later but can't be right now (temporary)

Do NOT exempt when:
- The rule is "inconvenient" but not operationally blocking
- You want to skip review (use `disabled_rules` for permanent non-compliance decisions)
- You don't understand the rule's impact (test first, exempt only if needed)

## Exemption schema

```hcl
exemptions = {
  "rule_id" = {
    reason                = "Why this rule cannot be applied"     # REQUIRED
    ticket                = "SEC-1234"                            # Recommended
    risk_status           = "ACCEPTED"                            # REQUIRED
    compensating_controls = "What mitigates the risk instead"     # Optional (required for ACCEPTED_WITH_COMPENSATING_CONTROLS)
    reviewer              = "name@example.com"                    # Recommended
    review_date           = "2026-12-01"                          # Optional (ISO date for periodic review)
    expires               = "2026-09-30"                          # Required for TEMPORARY
  }
}
```

## Risk statuses

| Status | Meaning | Expires required? |
|---|---|---|
| `UNDER_REVIEW` | Awaiting approval; rule not enforced | Yes (short window) |
| `ACCEPTED` | Approved permanent exemption | No |
| `TEMPORARY` | Approved for limited time | Yes |
| `ACCEPTED_WITH_COMPENSATING_CONTROLS` | Approved with mitigations | Recommended |

## Lifecycle

```
UNDER_REVIEW ──→ TEMPORARY ──(expires)──→ EXPIRED (CI blocks)
    │                │
    └────────────────┴──→ ACCEPTED (permanent)
    │
    └──→ ACCEPTED_WITH_COMPENSATING_CONTROLS (permanent with mitigations)
```

## CI enforcement

- `TEMPORARY` exemptions with `expires` in the past → **PR fails**
- Exemptions without `ticket` → **CI warning**
- Exemptions without `reviewer` → **CI warning**
- Exemptions without `reason` → **Terraform validation fails** (required field)

## Review cadence

Schedule exemption review at least quarterly:
1. Run `python scripts/check_exemptions.py --modules-dir modules/ --report-json exemptions.json`
2. Review each exemption: still valid? compensating controls still in place?
3. Update `review_date` or remove expired exemptions
4. Open PR with updated exemption state

## Exemption report

`terraform plan` outputs exemption summary. CI generates `exemptions-report.json` for GRC tooling:

```json
{
  "cis_lvl1_macos_26": {
    "os_dictation_disable": {
      "reason": "Clinical staff require dictation for EHR workflows",
      "ticket": "SEC-4521",
      "risk_status": "ACCEPTED",
      "timestamp": "2026-06-15T07:00:00Z"
    }
  }
}
```

## Anti-patterns

1. **Exempting without a ticket**: No audit trail. CI warns.
2. **Using TEMPORARY as a permanent workaround**: Set review_date; actually review it.
3. **Exempting entire baselines**: If you need to exempt more than 20% of rules, you've selected the wrong baseline. Choose a lower impact level instead.
4. **Copy-pasting exemption reasons**: Each exemption should have a specific, truthful justification.
```

---

### Skill 4: `add-compliance-baseline`

**Name**: `add-compliance-baseline`
**Trigger**: "add baseline", "new compliance framework", "add mSCP baseline", "new benchmark"
**Purpose**: Guide developers through adding support for a new mSCP baseline or a new macOS version to the pipeline.

**Contents**:

```markdown
# Adding a Compliance Baseline

Extend the pipeline to support a new mSCP baseline or macOS version.

## Adding a new baseline

When NIST mSCP adds a new baseline (e.g., a new framework or country-specific baseline):

1. Verify the baseline exists in the mSCP repo:
   ```bash
   git clone -b tahoe https://github.com/usnistgov/macos_security.git /tmp/mscp
   ls /tmp/mscp/baselines/
   ```

2. Add the baseline key to the generator config:
   ```python
   # scripts/generate_tf_compliance.py
   SUPPORTED_BASELINES = {
       # ... existing baselines ...
       "new_baseline_key": {
           "display_name": "New Framework Display Name",
           "category": "government",  # government | industry | international
       }
   }
   ```

3. Run the generator locally to produce baseline modules:
   ```bash
   python scripts/generate_tf_compliance.py \
     --mscp-path /tmp/mscp \
     --output modules/compliance \
     --baseline new_baseline_key
   ```

4. Verify generated modules:
   ```bash
   for dir in modules/compliance/new_baseline_key/macos_*/; do
     (cd "$dir" && terraform init -backend=false && terraform validate)
   done
   ```

5. Add an example to `examples/compliance-only/main.tf`

6. Open PR with baseline description and rule count

## Adding a new macOS version

When Apple releases a new macOS and mSCP creates a corresponding branch:

1. Add the version to the supported list:
   ```python
   # scripts/generate_tf_compliance.py
   SUPPORTED_VERSIONS = {
       "14": {"name": "Sonoma", "min": "14.0", "branch": "sonoma"},
       "15": {"name": "Sequoia", "min": "15.0", "branch": "sequoia"},
       "26": {"name": "Tahoe", "min": "26.0", "branch": "tahoe"},
       "27": {"name": "NewOS", "min": "27.0", "branch": "newos_branch"},
   }
   ```

2. Run the generator for all baselines against the new version:
   ```bash
   python scripts/generate_tf_compliance.py \
     --mscp-path /tmp/mscp \
     --output modules/compliance \
     --version 27
   ```

3. Update the Foundation `os-version-smart-groups` module to include the new OS.

4. Verify and open PR.

## Adding custom rules to a baseline

1. Create a custom rule override in `modules/compliance/{baseline}/macos_{version}/overrides.tf`:
   ```hcl
   locals {
     custom_rules = {
       "my_org_custom_rule" = {
         title       = "My Org Custom Rule"
         description = "Additional control not in upstream mSCP"
         severity    = "medium"
       }
     }
   }
   ```

2. Reference in the benchmark's `rules` block.

3. Document the custom rule's purpose and NIST 800-53 mapping in a comment.

## Anti-patterns

1. **Adding a baseline without testing generation**: Always run `terraform validate` locally.
2. **Skipping the example**: Every new baseline needs a usage example so consumers can discover it.
3. **Hardcoding baseline lists in multiple places**: The generator config is the single source of truth.
```

---

### Skill 5: `ci-pipeline-operations`

**Name**: `ci-pipeline-operations`
**Trigger**: "compliance update", "trigger CI", "check mSCP releases", "pipeline status", "force regeneration"
**Purpose**: Guide operators through CI pipeline operations — triggering, monitoring, and troubleshooting.

**Contents**:

```markdown
# CI Pipeline Operations

Operate the automated compliance baseline and foundation update pipelines.

## Scheduled behavior

- **Compliance update**: Weekly Monday 06:00 UTC. Polls mSCP releases. Opens PR if new revisions found.
- **Foundation update**: Monthly first Monday 06:00 UTC. Checks for PPPC bundle ID updates and provider version bumps.
- **Exemption check**: Every push and PR. Validates exemption expiration and completeness.

## Manual triggers

### Trigger compliance check on-demand

```bash
gh workflow run compliance-update.yml \
  --ref main \
  -f mscp_branch=tahoe
```

Omit `mscp_branch` or set to `all` to check all branches.

### Force regeneration for a specific branch

```bash
gh workflow run compliance-update.yml \
  --ref main \
  -f mscp_branch=sequoia
```

This re-generates even if no new release is detected (useful for testing generator changes).

### Trigger foundation update

```bash
gh workflow run foundation-update.yml --ref main
```

## Checking pipeline status

```bash
gh run list --workflow=compliance-update.yml --limit 5
gh run view {run_id}
```

## Troubleshooting

### Generator fails

1. Check if mSCP repo is accessible:
   ```bash
   gh api repos/usnistgov/macos_security/releases/latest
   ```

2. Check if mSCP container image is available:
   ```bash
   docker pull ghcr.io/usnistgov/mscp_2.0:latest
   ```

3. Run generator locally to reproduce:
   ```bash
   git clone -b tahoe https://github.com/usnistgov/macos_security.git /tmp/mscp
   python scripts/generate_tf_compliance.py \
     --mscp-path /tmp/mscp \
     --output /tmp/test-output \
     --branch tahoe
   ```

### Terraform validate fails on generated module

1. Check if the Jamf Platform provider schema changed:
   ```bash
   terraform providers schema -json | jq '.provider_schemas["registry.terraform.io/Jamf-Concepts/jamfplatform"]'
   ```

2. Compare against the generated resource shape in TECH.md.

### Exemption check blocks PR

1. Read the CI log for the specific exemption that failed.
2. Either:
   - Remove the expired exemption and enable the rule, OR
   - Extend the `expires` date with updated justification, OR
   - Change `risk_status` to `ACCEPTED` if it should be permanent.

### Multiple compliance PRs open simultaneously

This happens when multiple mSCP branches release simultaneously. Review and merge each PR independently. They target different module directories and won't conflict.

## Anti-patterns

1. **Merging compliance PRs without reviewing the changelog**: New rules may conflict with existing exemptions.
2. **Force-regenerating in production**: Test locally first with `--output /tmp/test-output`.
3. **Ignoring exemption check failures**: Expired TEMPORARY exemptions are a real compliance gap.
```

---

## Repository Governance Files

### CONTRIBUTING.md

```markdown
# Contributing

## Scope

This repository contains two sets of Terraform modules:
- **Compliance modules** (`modules/compliance/`) — auto-generated from NIST mSCP baselines
- **Foundation modules** (`modules/foundation/`) — hand-authored Jamf Pro scaffolding

## Before you contribute

1. Check existing issues and PRs for duplicates
2. For compliance modules: changes to generated code should go into the generator (`scripts/generate_tf_compliance.py`), not into generated files directly
3. For foundation modules: changes are welcome but should follow existing patterns

## Development setup

```bash
# Clone with specs
git clone https://github.com/your-org/jamf_mscp_tf.git
cd jamf_mscp_tf

# Install Python dependencies for generator scripts
python3 -m venv .venv
source .venv/bin/activate
pip install pyyaml jinja2

# Install Terraform
brew install terraform  # or via mise: mise install terraform
```

## Making changes

### Compliance module changes

1. Modify `scripts/generate_tf_compliance.py`
2. Run locally: `python scripts/generate_tf_compliance.py --mscp-path /path/to/mscp --output /tmp/test`
3. Verify: `terraform validate` on generated output
4. Write/update unit tests in `tests/`
5. Open PR with before/after example of generated output

### Foundation module changes

1. Modify the module directly in `modules/foundation/{module}/`
2. Update `examples/foundation-only/main.tf` if the interface changes
3. Run `terraform fmt -recursive` and `terraform validate`
4. Test against a Jamf Pro staging instance
5. Open PR

### Adding a skill

1. Create `.agents/skills/{skill-name}/SKILL.md`
2. Follow the existing skill format (PHASE-based, with anti-patterns)
3. Reference the skill in `AGENTS.md`
4. Open PR

## PR requirements

- PR title follows conventional commits: `compliance:`, `foundation:`, `ci:`, `docs:`, `spec:`
- Generated compliance PRs are exempt from the conventional title requirement (they use `compliance:` automatically)
- All changes pass `terraform fmt -check -recursive` and `terraform validate`
- Exemption check CI passes
- At least one review from a CODEOWNER

## Testing

```bash
# Python unit tests
pytest tests/

# Terraform validation (all modules)
for dir in modules/compliance/*/macos_*/ modules/foundation/*/; do
  (cd "$dir" && terraform init -backend=false && terraform validate)
done

# Exemption check
python scripts/check_exemptions.py --modules-dir modules/ --enforce-expiry false
```

## Code Style

### HCL/Terraform
- `terraform fmt` is the authority
- Use `_` for resource names (not `-`)
- Variables: lowercase with underscores
- Outputs: include `description`
- Comments: explain *why*, not *what*

### Python
- Type hints on all function signatures
- Docstrings for public functions
- ruff for linting/formatting

### YAML (skills, configs)
- 2-space indent
- Comments above complex blocks, not inline
```

---

### LICENSE

Apache 2.0 — standard for infrastructure/module repositories, compatible with the MPL-2.0 licensed Terraform providers this project depends on (`deploymenttheory/jamfpro` is MPL-2.0, `Jamf-Concepts/jamfplatform` is MPL-2.0). The mSCP project itself uses a Creative Commons Attribution 4.0 International license, but this project is independent tooling that consumes mSCP outputs.

### CODEOWNERS

```
# Compliance pipeline + generator
scripts/generate_tf_compliance.py  @engineering-team
scripts/generate_changelog.py      @engineering-team
scripts/detect_mscp_releases.py    @engineering-team

# Foundation modules
modules/foundation/                @macadmin-team

# CI/CD
.github/workflows/                 @devops-team

# Specs (require review for scope changes)
specs/                             @engineering-team @security-team

# Agent configuration
.agents/                           @engineering-team
AGENTS.md                          @engineering-team
```

### SECURITY.md

```markdown
# Security Policy

## Reporting a Vulnerability

If you discover a security issue in these modules (e.g., a misconfigured security control that weakens a macOS security posture, or a pipeline vulnerability), please report it privately:

1. **DO NOT** open a public issue
2. Email security@your-org.com with details
3. Include: affected module, version, description, reproduction steps

## Scope

Security issues include:
- Incorrect compliance rule mappings (rule says "enforce screensaver" but generates "allow screensaver disable")
- Missing rules from a baseline
- Pipeline vulnerabilities (workflow injection, secret exposure)
- Exemption bypass (exemption processing logic allows rules to be silently skipped)

## Out of scope

- Issues in upstream NIST mSCP rules (report to https://github.com/usnistgov/macos_security)
- Issues in Jamf Platform or Jamf Pro (report to Jamf support)
- Issues in Terraform providers (report to respective provider repositories)

## Supported versions

Only the latest tagged release is supported. Generated modules track mSCP versions; always use the latest.
```

---

### .gitignore

```gitignore
# Terraform
.terraform/
*.tfstate
*.tfstate.*
terraform.tfvars
override.tf
override.tf.json
.terraform.lock.hcl

# Python
.venv/
__pycache__/
*.pyc
*.pyo
.eggs/
dist/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# CI artifacts
.ci/*.log
exemptions-report.json

# Secrets (in case someone copies credentials here)
*.pem
*.key
credentials.json

# Build output
/build/
/tmp/
```

---

### CHANGELOG.md (initial)

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial compliance module generation pipeline for 16 NIST mSCP baselines
- macAdmin Foundation modules (8 modules) for new Jamf Pro tenant setup
- Exemption tracking system with audit trail and CI enforcement
- GitHub Actions CI: compliance update, foundation update, exemption check
- Agent skills: compliance-baseline-usage, foundation-setup, manage-exemptions, add-compliance-baseline, ci-pipeline-operations
- Product and technical specifications (PRODUCT.md, TECH.md, REPO.md)

[Unreleased]: https://github.com/your-org/jamf_mscp_tf/compare/v0.1.0...HEAD
```

---

## AGENTS.md

This is the canonical OpenCode agent configuration file. Lives at repo root.

```markdown
# AGENTS.md — jamf_mscp_tf

## Project Identity

This repository generates and maintains Terraform modules for deploying NIST mSCP compliance baselines and macAdmin foundation scaffolding to Jamf Pro. It is a meta-repository: most compliance code is auto-generated by Python scripts that consume the upstream `usnistgov/macos_security` repository.

## Repository topology

```
modules/compliance/   ← AUTO-GENERATED by scripts/generate_tf_compliance.py
modules/foundation/   ← HAND-AUTHORED (do not regenerate)
scripts/              ← Python generators and CI helpers
specs/                ← Product, tech, and repo specifications
.agents/skills/       ← Agent skills for project operations
examples/             ← Consumer-facing usage examples
```

## Critical invariant

**Never edit generated compliance modules directly.** Changes to `modules/compliance/` must go through `scripts/generate_tf_compliance.py`. Direct edits will be overwritten on the next CI run.

Foundation modules in `modules/foundation/` are hand-authored — edit those directly.

## Working in this repository

### Before starting any task

1. Check if the change affects generated or hand-authored code
2. Read the relevant spec in `specs/mscp-terraform-pipeline/`
3. For compliance changes: read `TECH.md` section on generator logic
4. For foundation changes: read `PRODUCT.md` section on Variant B

### Making code changes

- Generated code path: `scripts/generate_tf_compliance.py` → `modules/compliance/`
- Test locally: `pytest tests/`
- Validate Terraform: `terraform validate` on affected modules
- Run exemption check: `python scripts/check_exemptions.py --modules-dir modules/`

### Quality gates (all PRs)

1. `terraform fmt -check -recursive` passes
2. `terraform validate` passes on all changed modules
3. Exemption check CI passes (no expired exemptions, no missing tickets)
4. Python tests pass: `pytest tests/`
5. Ruff linting passes: `ruff check scripts/`

### When to update specs

- PRODUCT.md: when user-facing behavior changes (new baseline support, new exemption status, new module)
- TECH.md: when architecture changes (new generator, new CI workflow, change in provider)
- REPO.md: when governance or agent configuration changes (new skill, new CODEOWNER, policy change)

### Commits and PRs

- Follow conventional commits: `compliance:`, `foundation:`, `ci:`, `docs:`, `spec:`, `skill:`
- Compliance PRs opened by CI use `compliance:` prefix automatically
- Include co-author line: `Co-Authored-By: Oz <oz-agent@warp.dev>`
- PR description must reference any affected spec sections

### Agent skills available

This repository includes localized skills in `.agents/skills/`:

| Skill | When to use |
|---|---|
| `compliance-baseline-usage` | Deploying/monitoring compliance baselines |
| `foundation-setup` | Setting up a new Jamf Pro tenant |
| `manage-exemptions` | Declaring/reviewing security control exemptions |
| `add-compliance-baseline` | Extending the pipeline for new baselines/OS versions |
| `ci-pipeline-operations` | Operating the CI pipeline |

Load a skill with the `skill` tool when a task matches its description.

### Upstream dependencies

| Dependency | Version | Purpose |
|---|---|---|
| NIST mSCP | Branch-tagged releases | Source of compliance rules |
| deploymenttheory/jamfpro | >= 0.36.0 | Foundation module provider |
| Jamf-Concepts/jamfplatform | >= 0.17.0 | Compliance benchmark provider |
| ghcr.io/usnistgov/mscp_2.0 | latest | CI container for generation |

### Environment variables

For local testing:
- `JAMFPLATFORM_CLIENT_ID` / `JAMFPLATFORM_CLIENT_SECRET` — Jamf Platform API credentials
- `JAMFPLATFORM_BASE_URL` — Region-specific API gateway (default: `https://us.apigw.jamf.com`)
- `TF_VAR_jamfpro_client_id` / `TF_VAR_jamfpro_client_secret` — Jamf Pro API credentials
- `TF_VAR_jamfpro_instance_fqdn` — Jamf Pro instance URL

Never commit these values. Use `terraform.tfvars` (gitignored) or environment variables.

### Project conventions

- Python: type hints, docstrings, ruff formatting, pytest
- HCL: `terraform fmt`, lowercase_with_underscores, descriptions on all outputs
- YAML: 2-space indent, comments above blocks
- Skills: PHASE-based structure with anti-patterns section
```

---

## Skill Architecture Notes

### Why skills are local to this repo

Skills in `.agents/skills/` are project-scoped and travel with the repository. Unlike the user's global skills in `~/.agents/skills/`, these are:
- Version-controlled alongside the code they document
- Updated when module interfaces change
- Discoverable by anyone who clones the repo

### Skill design principles

1. **PHASE-based structure**: Every skill follows PHASE 0 (pre-flight) → PHASE N (actions) → anti-patterns. This is inherited from the macOS Hardening skill pattern.
2. **Actionable, not descriptive**: Skills tell the agent *what to do*, not *what the thing is*. The specs handle description.
3. **Anti-patterns section required**: Every skill must list common mistakes. This is the highest-value section for agents.
4. **One skill per persona**: `compliance-baseline-usage` is for security operators; `add-compliance-baseline` is for pipeline developers. They serve different audiences.

### When to add a new skill

Add a skill when:
- A task requires 4+ sequential steps that agents frequently get wrong
- The task spans multiple modules or variants
- There are non-obvious failure modes (anti-patterns)
- The task will be performed by someone new to the project

Do NOT add a skill for:
- Single-command operations
- Tasks fully documented in README.md
- Trivial configuration changes

### Skill storage

```
.agents/skills/
├── compliance-baseline-usage/
│   └── SKILL.md
├── foundation-setup/
│   └── SKILL.md
├── manage-exemptions/
│   └── SKILL.md
├── add-compliance-baseline/
│   └── SKILL.md
└── ci-pipeline-operations/
    └── SKILL.md
```

---

## Success Criteria for REPO.md

- **Skill coverage**: Every major workflow (deploy compliance, deploy foundation, manage exemptions, add baseline, operate CI) has a dedicated skill.
- **Governance completeness**: CONTRIBUTING.md, LICENSE, CODEOWNERS, SECURITY.md, .gitignore, and CHANGELOG.md are defined with project-appropriate content.
- **AGENTS.md accuracy**: Agent configuration accurately describes the repository topology, critical invariants, quality gates, and upstream dependencies.
- **Skill testability**: Each skill's PHASE structure can be followed step-by-step by an agent without additional context.
- **Anti-pattern enforcement**: Every skill includes specific anti-patterns that CI or review processes should catch.

# PRODUCT.md — NIST mSCP → Jamf Pro Terraform Modules

## Problem Statement

Organizations using Jamf Pro to manage macOS fleets face two related but distinct problems:

1. **Compliance**: Security teams must deploy and track security baselines aligned to NIST SP 800-53, DISA STIG, CIS Benchmarks, and other frameworks. The NIST mSCP provides authoritative baseline definitions, but there is no automated path from mSCP releases to deployable Terraform configurations. Baselines are hand-picked, manually configured, and drift on every mSCP revision.

2. **Day-zero setup**: Every Jamf Pro tenant, regardless of compliance requirements, needs common scaffolding — categories, smart groups for OS version targeting, basic security profiles (FileVault, firewall, screensaver), software update enforcement, PPPC profiles, and device enrollment settings. Admins reinvent this per tenant.

## Solution

Two composable Terraform module variants in a single repository, both auto-generated and kept current via GitHub Actions:

- **Variant A — Compliance Baselines**: Terraform resources for the Jamf Platform Compliance Benchmark Engine, covering all 16 NIST mSCP baselines across 3 macOS versions. Auto-regenerates when mSCP releases new revisions.
- **Variant B — macAdmin Foundation**: Standard Jamf Pro scaffolding that every macadmin needs on a new tenant. Categories, smart groups, sensible security defaults, software update policies, PPPC profiles, and enrollment settings.

Both share a CI pipeline that polls for upstream changes and opens PRs. Both include a first-class **exemption tracking system** so operators can explicitly disable rules/profiles with an audit trail of why.

---

## Variant A — Compliance Baselines

### Architecture

Uses Jamf's native **Compliance Benchmark Engine** via the `Jamf-Concepts/jamfplatform` Terraform provider (`v0.17.0+`). Instead of generating `.mobileconfig` files and uploading them as configuration profiles, this approach leverages Jamf's server-side mSCP rule ingestion:

```
NIST mSCP Release → CI Pipeline reads rule metadata
                  → Generates jamfplatform_cbengine_benchmark resources
                  → Jamf Platform manages rule evaluation + enforcement
```

Each generated benchmark resource references the exact mSCP branch + revision, targets a device group (by OS version), and exposes per-rule enable/disable + ODV customization as Terraform variables.

### Supported baselines

#### Government Frameworks

| Baseline Key | Framework | Impact Level |
|---|---|---|
| `800-53r5_high` | NIST SP 800-53 Rev 5 | High |
| `800-53r5_moderate` | NIST SP 800-53 Rev 5 | Moderate |
| `800-53r5_low` | NIST SP 800-53 Rev 5 | Low |
| `800-53r5_privacy` | NIST SP 800-53 Rev 5 | Privacy |
| `800-171` | NIST SP 800-171 Rev 3 | — |
| `disa_stig` | DISA macOS STIG | — |
| `cmmc_lvl1` | CMMC 2.0 | Level 1 |
| `cmmc_lvl2` | CMMC 2.0 | Level 2 |
| `cnssi-1253_high` | CNSSI 1253 | High |
| `cnssi-1253_moderate` | CNSSI 1253 | Moderate |
| `cnssi-1253_low` | CNSSI 1253 | Low |
| `nlmapgov_base` | Netherlands BIO | Base |
| `nlmapgov_plus` | Netherlands BIO | Plus |
| `hicp_lp` | HICP Large Healthcare Organizations | — |


#### Industry & International

| Baseline Key | Framework | Level |
|---|---|---|
| `cis_lvl1` | CIS macOS Benchmark | Level 1 |
| `cis_lvl2` | CIS macOS Benchmark | Level 2 |
| `cisv8` | CIS Controls v8 | — |

### Supported macOS versions

| macOS | Version | mSCP Branch | Latest Release |
|---|---|---|---|
| Tahoe | 26.0 | `tahoe` | `tahoe_rev2` |
| Sequoia | 15.0 | `sequoia` | `sequoia_rev4` |
| Sonoma | 14.0 | `sonoma` | `sonoma_rev5` |

### Consumer experience

```hcl
module "cis_lvl1_tahoe" {
  source = "./modules/compliance/cis_lvl1/macos_26"

  enforcement_mode = "MONITOR_AND_ENFORCE"

  # Override organization-defined values
  rule_overrides = {
    "system_settings_time_server_configure" = {
      odv_value = "ntp.example.com"
    }
  }

  # Disable specific rules with audit justification
  exemptions = {
    "os_dictation_disable" = {
      reason      = "Clinical staff require dictation for EHR workflows"
      ticket      = "SEC-4521"
      risk_status = "ACCEPTED"
    }
    "os_airdrop_disable" = {
      reason      = "Field researchers share data between managed iPads and MacBooks"
      ticket      = "GRC-2025-089"
      risk_status = "ACCEPTED_WITH_COMPENSATING_CONTROLS"
      compensating_controls = "AirDrop restricted to managed devices only via MDM restriction profile; Bluetooth limited to device proximity range"
    }
  }
}
```

---

## Variant B — macAdmin Foundation

### What it is

A composable set of Terraform modules covering the standard Jamf Pro scaffolding that virtually every macadmin configures on a new tenant. Uses the `deploymenttheory/jamfpro` provider. Sensible, non-controversial defaults that follow community best practices.

### Modules

| Module | Resources Created | Purpose |
|---|---|---|
| `categories` | Jamf Pro categories | `Security`, `Productivity`, `Utilities`, `Communication`, `Browsers`, `Developer Tools` |
| `os-version-smart-groups` | Smart computer groups per OS version | `macOS 14 — Sonoma`, `macOS 15 — Sequoia`, `macOS 26 — Tahoe`, `macOS — Unsupported` |
| `security-baseline` | Configuration profiles | FileVault enforcement, firewall enable + stealth, screensaver password + 5-min timeout, Gatekeeper (App Store + identified devs), automatic login disable, password hints disable, guest account disable |
| `software-updates` | Configuration profiles | Auto-download, auto-install security updates, defer major OS upgrades 90 days, defer minor updates 14 days, enable Rapid Security Response |
| `pppc-screen-capture` | PPPC profile | Allow common collaboration tools screen capture access (Zoom, Slack, Teams, Google Chrome, Webex) |
| `pppc-accessibility` | PPPC profile | Allow common tools accessibility access |
| `device-enrollment` | ADE settings | Skip setup panes (Apple ID, Siri, Touch ID, Screen Time, Privacy, iCloud storage), require MDM enrollment, disallow MDM profile removal |
| `inventory-settings` | Jamf Pro settings | Collection frequency, software update collection, extension attribute collection |

### Consumer experience

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

  software_update_major_deferral_days = 90
  screensaver_idle_timeout_minutes    = 5
  pppc_tools = ["Zoom", "Slack", "Microsoft Teams", "Google Chrome", "Webex"]

  # Disable a module with justification
  exemptions = {
    "device_enrollment" = {
      reason      = "ADE token not yet provisioned — will re-enable in Q3"
      ticket      = "IT-7823"
      risk_status = "TEMPORARY"
    }
  }
}
```

---

## Exemption Tracking System (Both Variants)

Every rule, profile, and module supports an `exemptions` map. This is a first-class feature — not an afterthought — because compliance isn't about applying every control blindly; it's about making conscious, documented decisions about what to apply and what to waive.

### Exemption schema

```hcl
variable "exemptions" {
  type = map(object({
    reason                = string                 # Human-readable justification
    ticket                = optional(string)       # Issue tracker / change request reference
    risk_status           = string                 # ACCEPTED | TEMPORARY | ACCEPTED_WITH_COMPENSATING_CONTROLS | UNDER_REVIEW
    compensating_controls = optional(string)       # What mitigations are in place instead
    reviewer              = optional(string)       # Who approved the exemption
    review_date           = optional(string)       # ISO date for scheduled review
    expires               = optional(string)       # ISO date when exemption expires
  }))
  default     = {}
  description = "Exemptions with audit justification for compliance tracking"
}
```

### Status lifecycle

```
UNDER_REVIEW → ACCEPTED  (approved, in place permanently)
             → TEMPORARY  (approved, auto-expires on date)
             → ACCEPTED_WITH_COMPENSATING_CONTROLS  (approved with mitigations)
```

### What happens when an exemption is declared

1. **The rule/profile/module is not deployed.** Terraform conditionally excludes the resource.
2. **The exemption is rendered as a Terraform output** so it's visible in `terraform plan` and in CI logs.
3. **The exemption data is emitted as a JSON file** (`exemptions-report.json`) in the build output, machine-readable for GRC tools.
4. **Terraform plan shows a summary** of how many resources were excluded and why.

### Example: mixed baseline with exemptions

```hcl
module "80053_moderate_tahoe" {
  source = "./modules/compliance/800-53r5_moderate/macos_26"

  enforcement_mode = "MONITOR_AND_ENFORCE"

  exemptions = {
    "icloud_keychain_disable" = {
      reason      = "Users need iCloud Keychain for cross-device password sync in BYOD-optional program"
      ticket      = "GRC-2026-014"
      risk_status = "ACCEPTED"
      reviewer    = "jane.doe@example.com"
      review_date = "2026-12-01"
    }
    "os_iphone_mirroring_disable" = {
      reason      = "Engineering team uses iPhone mirroring for iOS app testing on Mac"
      ticket      = "ENG-4412"
      risk_status = "ACCEPTED_WITH_COMPENSATING_CONTROLS"
      compensating_controls = "iPhone Mirroring restricted to Developer VLAN (subnet 10.88.0.0/16) via network segmentation; only enrolled corporate iPhones permitted"
      reviewer    = "security-team@example.com"
    }
    "system_settings_bluetooth_disable" = {
      reason      = "Bluetooth required for wireless peripherals in open-plan office"
      ticket      = "IT-9012"
      risk_status = "TEMPORARY"
      expires     = "2026-09-30"
      reviewer    = "ciso@example.com"
    }
  }
}
```

### CI enforcement

If an exemption has `expires` set and the current date is past it, the CI pipeline **fails the PR** with a clear message: `Exemption for rule {id} has expired ({date}). Either remove the exemption and enable the rule, or extend the expiration with updated justification.` This prevents "temporary" waivers from becoming permanent silent gaps.

---

## Shared Infrastructure

### CI Pipeline

- Runs on schedule (quarterly) + on-demand (`workflow_dispatch`)
- Two independent update paths:
  - **Variant A**: Polls mSCP releases API for new tags. On new release, regenerates compliance modules and opens PR.
  - **Variant B**: Polls for PPPC bundle ID updates, provider version bumps. Updates monthly.
- PR includes: changed files list, `terraform plan` diff, rule-level changelog (Variant A), exemption summary
- Expired exemption check runs on every PR and push

### Module registry layout

```
modules/
├── compliance/                     # Variant A
│   ├── 800-53r5_high/
│   │   ├── macos_14/
│   │   ├── macos_15/
│   │   └── macos_26/
│   ├── 800-53r5_moderate/
│   │   └── ... (same structure)
│   ├── cis_lvl1/
│   │   └── ...
│   └── ... (all 16 baselines)
│
└── foundation/                     # Variant B
    ├── categories/
    ├── os-version-smart-groups/
    ├── security-baseline/
    ├── software-updates/
    ├── pppc-screen-capture/
    ├── pppc-accessibility/
    ├── device-enrollment/
    └── inventory-settings/
```

### Provider requirements

| Variant | Provider | Purpose |
|---|---|---|
| A — Compliance | `Jamf-Concepts/jamfplatform` >= 0.17.0 | Compliance Benchmark Engine, device groups |
| B — Foundation | `deploymenttheory/jamfpro` >= 0.36.0 | Configuration profiles, categories, enrollment, inventory |

Both use OAuth2 authentication with `client_id` + `client_secret`.

---

## Success Criteria

- **Completeness (Variant A)**: All 16 mSCP baselines × 3 macOS versions = 48 generated modules, each referencing the correct mSCP branch + revision.
- **Completeness (Variant B)**: All 8 foundation modules cover the standard "new Jamf tenant" checklist.
- **Freshness**: A new mSCP release produces a compliance PR within one CI cycle. Foundation updates arrive monthly.
- **Deployability**: Both variants pass `terraform validate` and `terraform plan` against a real Jamf Pro instance.
- **Auditability**: Every generated benchmark resource includes mSCP baseline name, branch, revision, and rule count in its description. Every exemption appears in `terraform plan` output, CI logs, and `exemptions-report.json`.
- **Exemption enforcement**: Expired temporary exemptions block PRs. Exemptions without tickets or reviewer attribution produce CI warnings.
- **Backward compatibility**: Consumers pin to git tags or commit SHAs. Updates arrive as opt-in PR merges.
- **No vendor lock-in**: Foundation uses `deploymenttheory/jamfpro` (community provider). Compliance uses `Jamf-Concepts/jamfplatform` (Jamf-published provider). Both on the Terraform Registry.

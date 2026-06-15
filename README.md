# jamf_mscp_tf

Terraform modules that automate NIST mSCP compliance baselines and macAdmin foundation scaffolding for Jamf Pro — all kept current via GitHub Actions CI.

## Problem

Organizations using Jamf Pro to manage macOS fleets face two distinct but related problems:

1. **Compliance**: Security teams must deploy and track security baselines aligned to NIST SP 800-53, DISA STIG, CIS Benchmarks, and other frameworks. The NIST mSCP provides authoritative baseline definitions, but there is no automated path from mSCP releases to deployable Terraform configurations.

2. **Day-zero setup**: Every Jamf Pro tenant needs common scaffolding — categories, smart groups for OS version targeting, basic security profiles, software update enforcement, PPPC profiles, and device enrollment settings. Admins reinvent this per tenant.

## Solution

Two composable Terraform module variants in a single repository:

- **Variant A — Compliance Baselines**: Terraform resources for the Jamf Platform Compliance Benchmark Engine, covering all 16 NIST mSCP baselines across 3 macOS versions. Auto-regenerates when mSCP releases new revisions.

- **Variant B — macAdmin Foundation**: Standard Jamf Pro scaffolding for new tenants. Categories, smart groups, sensible security defaults, software update policies, PPPC profiles, and enrollment settings.

Both share a CI pipeline that polls for upstream changes and opens PRs. Both include a first-class exemption tracking system so operators can explicitly waive rules with an audit trail.

## Quick Start

### Variant A — Deploy a compliance baseline

```hcl
module "cis_lvl1_tahoe" {
  source = "./modules/compliance/cis_lvl1/macos_26"

  enforcement_mode = "MONITOR_AND_ENFORCE"

  exemptions = {
    "os_dictation_disable" = {
      reason      = "Clinical staff require dictation for EHR workflows"
      ticket      = "SEC-4521"
      risk_status = "ACCEPTED"
    }
  }
}
```

Start with `MONITOR` mode on first deploy. Switch to `MONITOR_AND_ENFORCE` after reviewing the compliance report.

### Variant B — Scaffold a new Jamf Pro tenant

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

### Both together

```hcl
module "foundation" { source = "./modules/foundation" /* ... */ }
module "cis_l1"     { source = "./modules/compliance/cis_lvl1/macos_26" /* ... */ }
module "80053_mod"  { source = "./modules/compliance/800-53r5_moderate/macos_26" /* ... */ }
```

## Supported Baselines

16 NIST mSCP baselines across 3 macOS versions (Sonoma 14, Sequoia 15, Tahoe 26): NIST 800-53r5 (High/Moderate/Low/Privacy), 800-171, DISA STIG, CMMC L1/L2, CNSSI 1253 (High/Moderate/Low), Netherlands BIO (Base/Plus), CIS L1/L2, CIS v8.

## Foundation Modules

| Module | Purpose |
|---|---|
| `categories` | Standard Jamf Pro categories |
| `os-version-smart-groups` | Per-OS-version smart groups |
| `security-baseline` | FileVault, firewall, screensaver, Gatekeeper |
| `software-updates` | Auto-update policies with deferral windows |
| `pppc-screen-capture` | PPPC profile for collaboration tools |
| `pppc-accessibility` | PPPC accessibility profile |
| `device-enrollment` | ADE PreStage enrollment settings |
| `inventory-settings` | Check-in frequency and collection config |

## Module Registry Layout

```
modules/
├── compliance/                     # Variant A — auto-generated
│   ├── 800-53r5_high/
│   │   ├── macos_14/
│   │   ├── macos_15/
│   │   └── macos_26/
│   ├── 800-53r5_moderate/
│   ├── cis_lvl1/
│   └── ... (all 16 baselines)
│
└── foundation/                     # Variant B — hand-authored
    ├── categories/
    ├── os-version-smart-groups/
    ├── security-baseline/
    ├── software-updates/
    ├── pppc-screen-capture/
    ├── pppc-accessibility/
    ├── device-enrollment/
    └── inventory-settings/
```

## Exemption Tracking

Every rule, profile, and module supports an `exemptions` map. Exemptions are machine-readable, appear in `terraform plan` output, are emitted as JSON for GRC tooling, and expired temporary exemptions block PRs in CI.

## CI Pipeline

- **Compliance update** — Weekly Monday 06:00 UTC. Polls mSCP releases, regenerates modules, opens PR with changelog.
- **Foundation update** — Monthly. Checks for PPPC bundle ID updates and provider version bumps.
- **Exemption check** — Every push and PR. Validates exemption expiration and completeness.

## Success Criteria

- 48 generated compliance modules (16 baselines × 3 macOS versions)
- 8 hand-authored foundation modules
- All modules pass `terraform validate`
- Expired temporary exemptions block PRs
- Consumer pins to git tags for backward compatibility

## Full Specs

- [PRODUCT.md](specs/mscp-terraform-pipeline/PRODUCT.md) — user-facing behavior, variants, exemption system
- [TECH.md](specs/mscp-terraform-pipeline/TECH.md) — architecture, generator logic, CI design, key decisions
- [REPO.md](specs/mscp-terraform-pipeline/REPO.md) — skills, governance, agent configuration

## License

Apache 2.0. See [LICENSE](LICENSE).

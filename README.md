# jamf_mscp_tf

Terraform modules for deploying NIST mSCP compliance baselines and macAdmin foundation scaffolding into Jamf Pro. 16 compliance frameworks × 3 macOS versions — all kept current via CI.

## Prerequisites

- **Terraform** ≥ 1.9
- **Jamf Platform API** credentials (client ID + secret) — for compliance baselines
- **Jamf Pro API** credentials (client ID + secret + instance FQDN) — for foundation modules

Create API credentials in Jamf Pro under **Settings → API roles and clients**.

## Authentication

Set credentials as environment variables (never commit them to the repo):

```bash
export TF_VAR_jamfplatform_client_id="your-platform-client-id"
export TF_VAR_jamfplatform_client_secret="your-platform-client-secret"
export TF_VAR_jamfplatform_base_url="https://us.apigw.jamf.com"

export TF_VAR_jamfpro_client_id="your-pro-client-id"
export TF_VAR_jamfpro_client_secret="your-pro-client-secret"
export TF_VAR_jamfpro_instance_fqdn="your-org.jamfcloud.com"
```

Or create a `terraform.tfvars` file (gitignored):

```hcl
jamfplatform_client_id     = "your-platform-client-id"
jamfplatform_client_secret = "your-platform-client-secret"
jamfpro_client_id          = "your-pro-client-id"
jamfpro_client_secret      = "your-pro-client-secret"
jamfpro_instance_fqdn      = "your-org.jamfcloud.com"
```

If you use 1Password, reference secrets directly with `op://` references.

## Quick start: deploy a compliance baseline

1. Clone this repo into your Terraform project.
2. Set your Jamf Platform credentials (see above).
3. Drop this into `main.tf`:

```hcl
terraform {
  required_version = ">= 1.9.0"
  required_providers {
    jamfplatform = {
      source  = "Jamf-Concepts/jamfplatform"
      version = ">= 0.17.0"
    }
  }
}

provider "jamfplatform" {
  client_id     = var.jamfplatform_client_id
  client_secret = var.jamfplatform_client_secret
  base_url      = var.jamfplatform_base_url
}

module "cis_l1" {
  source = "./modules/compliance/cis_lvl1/macos_26"

  enforcement_mode = "MONITOR"
}
```

4. Run the plan to see what would change:

```bash
terraform init
terraform plan
```

5. If the plan looks correct, apply it:

```bash
terraform apply
```

Start with `MONITOR` mode. It deploys the benchmark in audit-only mode — no enforcement, just reporting. Switch to `MONITOR_AND_ENFORCE` after you've reviewed the compliance report in Jamf Pro.

## Quick start: scaffold a new Jamf Pro tenant

Foundation modules use the `jamfpro` provider:

```hcl
terraform {
  required_version = ">= 1.9.0"
  required_providers {
    jamfpro = {
      source  = "deploymenttheory/jamfpro"
      version = ">= 0.36.0"
    }
  }
}

provider "jamfpro" {
  client_id             = var.jamfpro_client_id
  client_secret         = var.jamfpro_client_secret
  jamfpro_instance_fqdn = var.jamfpro_instance_fqdn
  auth_method           = "oauth2"
}

# Enable the modules you need. Start with these:
module "categories"                { source = "./modules/foundation/categories";                enable_categories        = true }
module "os_version_smart_groups"   { source = "./modules/foundation/os-version-smart-groups";  enable_smart_groups       = true }
module "security_baseline"         { source = "./modules/foundation/security-baseline";        enable_security_baseline  = true }
module "software_updates"          { source = "./modules/foundation/software-updates";         enable_software_updates   = true }
module "inventory_settings"        { source = "./modules/foundation/inventory-settings";       enable_inventory_settings = true }
```

## I already manage Jamf Pro — how do I migrate to Terraform?

See **[docs/MIGRATION.md](docs/MIGRATION.md)** for a step-by-step guide covering:
- Importing existing configuration profiles as Terraform resources
- Layering these modules on top of an existing tenant without breaking things
- Using `terraform plan` to validate before applying
- Handling naming conflicts with existing resources

The short version: start by deploying the foundation modules in a dry-run, review what `terraform plan` says it would create, then selectively import or adopt resources. [jamformer](https://github.com/Jamf-Concepts/jamformer) can help you discover and export your existing Jamf configuration as Terraform scaffolding.

## Module reference

### Compliance baselines (Variant A)

| Module path | Framework | Rules |
|---|---|---|
| `compliance/800-53r5_high/macos_{14,15,26}` | NIST SP 800-53 Rev 5 — High | — |
| `compliance/800-53r5_moderate/macos_{14,15,26}` | NIST SP 800-53 Rev 5 — Moderate | — |
| `compliance/800-53r5_low/macos_{14,15,26}` | NIST SP 800-53 Rev 5 — Low | — |
| `compliance/800-53r5_privacy/macos_{14,15,26}` | NIST SP 800-53 Rev 5 — Privacy | pending upstream |
| `compliance/800-171/macos_{14,15,26}` | NIST SP 800-171 Rev 3 | — |
| `compliance/disa_stig/macos_{14,15,26}` | DISA macOS STIG | — |
| `compliance/cmmc_lvl1/macos_{14,15,26}` | CMMC 2.0 — Level 1 | — |
| `compliance/cmmc_lvl2/macos_{14,15,26}` | CMMC 2.0 — Level 2 | — |
| `compliance/cnssi-1253_high/macos_{14,15,26}` | CNSSI 1253 — High | — |
| `compliance/cnssi-1253_moderate/macos_{14,15,26}` | CNSSI 1253 — Moderate | — |
| `compliance/cnssi-1253_low/macos_{14,15,26}` | CNSSI 1253 — Low | — |
| `compliance/nlmapgov_base/macos_{14,15,26}` | Netherlands BIO — Base | — |
| `compliance/nlmapgov_plus/macos_{14,15,26}` | Netherlands BIO — Plus | — |
| `compliance/hicp_lp/macos_{14,15,26}` | HICP Large Healthcare | — |
| `compliance/cis_lvl1/macos_{14,15,26}` | CIS macOS Benchmark — Level 1 | — |
| `compliance/cis_lvl2/macos_{14,15,26}` | CIS macOS Benchmark — Level 2 | — |
| `compliance/cisv8/macos_{14,15,26}` | CIS Controls v8 | — |

Each compliance module accepts:
- `enforcement_mode` — `"MONITOR"` or `"MONITOR_AND_ENFORCE"`
- `disabled_rules` — rule IDs to permanently disable
- `rule_overrides` — organization-defined value overrides per rule
- `exemptions` — waive rules with audit justification

### Foundation modules (Variant B)

| Module path | What it creates | Key variables |
|---|---|---|
| `foundation/categories` | Standard Jamf Pro categories | `enable_categories` |
| `foundation/os-version-smart-groups` | Smart groups per macOS version | `enable_smart_groups` |
| `foundation/security-baseline` | FileVault, firewall, screensaver, Gatekeeper | `enable_security_baseline`, `screensaver_idle_timeout_minutes` |
| `foundation/software-updates` | DDM-native update deferral policies | `enable_software_updates`, `ddm_update_action`, `ddm_max_deferrals` |
| `foundation/pppc-screen-capture` | PPPC profile for collaboration tools | `enable_pppc_screen_capture`, `pppc_tools` |
| `foundation/pppc-accessibility` | PPPC accessibility profile | `enable_pppc_accessibility`, `pppc_tools` |
| `foundation/device-enrollment` | ADE PreStage enrollment settings | `enable_device_enrollment` |
| `foundation/inventory-settings` | Check-in frequency and collection config | `enable_inventory_settings`, `checkin_frequency_minutes` |
| `foundation/intelligence-settings` | Apple Intelligence DDM controls (macOS 26.4+) | `enable_intelligence_settings`, `use_legacy_profile` |
| `foundation/external-intelligence-settings` | Third-party AI integration controls (macOS 26.4+) | `enable_external_intelligence_settings`, `use_legacy_profile` |

## Exemption tracking

Every module supports an `exemptions` map. Instead of commenting out rules, declare why they're waived:

```hcl
exemptions = {
  "os_airdrop_disable" = {
    reason      = "Field researchers share data between managed devices"
    ticket      = "GRC-2025-089"
    risk_status = "ACCEPTED"
  }
  "system_settings_bluetooth_disable" = {
    reason      = "Bluetooth required for wireless peripherals"
    ticket      = "IT-9012"
    risk_status = "TEMPORARY"
    expires     = "2026-09-30"
    reviewer    = "ciso@example.com"
  }
}
```

Exemptions appear in `terraform plan`, are emitted as JSON for GRC tools, and expired temporary exemptions block CI merges.

## Safe deployment checklist

1. **Always `plan` first.** Run `terraform plan` and review every resource that would be created or changed.
2. **Start with `MONITOR`.** Compliance baselines default to audit-only mode. Switch to enforcement after reviewing reports.
3. **Use `terraform import` for existing resources.** Don't let Terraform recreate things you already have. See the migration guide.
4. **Test on a staging tenant** if you have one.
5. **Pin your dependency** on a specific git tag or commit SHA. Updates arrive as opt-in PR merges — you're never force-upgraded.
6. **Check CI exemption results.** Expired exemptions block PRs. Keep your `expires` dates honest.

## CI pipeline

- **Compliance update** — quarterly. Polls mSCP releases, regenerates modules, opens a PR with a rule-level changelog.
- **Foundation update** — monthly. Checks for PPPC bundle ID updates and provider version bumps.
- **Exemption check** — every push and PR. Validates exemption expiry dates and completeness.

You can also trigger compliance and foundation updates manually via `workflow_dispatch`.

## Docs

| Document | What it covers |
|---|---|
| [docs/MIGRATION.md](docs/MIGRATION.md) | Importing existing Jamf configs into Terraform |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Development setup, code style, PR requirements |
| [SECURITY.md](SECURITY.md) | Reporting vulnerabilities |
| [specs/mscp-terraform-pipeline/PRODUCT.md](specs/mscp-terraform-pipeline/PRODUCT.md) | Full product spec — all baselines, exemption system, success criteria |
| [specs/mscp-terraform-pipeline/TECH.md](specs/mscp-terraform-pipeline/TECH.md) | Architecture — generator logic, CI design, key decisions |
| [LICENSE](LICENSE) | Apache 2.0 |

## License

Apache 2.0. See [LICENSE](LICENSE).

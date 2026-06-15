---
name: foundation-setup
description: Guide for deploying macAdmin Foundation modules for a new Jamf Pro tenant. Triggers on "new Jamf tenant", "Jamf foundation", "macAdmin setup", "Jamf scaffolding", "day zero Jamf".
---

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

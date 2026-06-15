---
name: compliance-baseline-usage
description: Guide for selecting, configuring, and deploying NIST mSCP compliance baselines via Jamf Platform Compliance Benchmark Engine. Triggers on "compliance baseline", "mSCP benchmark", "deploy CIS", "deploy STIG", "NIST 800-53 module".
---

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

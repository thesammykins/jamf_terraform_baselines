# CMMC 2.0 — Level 2 — macOS 14

## Overview

- **Baseline key**: `cmmc_lvl2`
- **Category**: government
- **macOS version**: 14 (14.0+)
- **mSCP branch**: `sonoma`
- **mSCP revision**: `rev5.0`
- **Rule count**: 198

## Severity distribution

- **high**: 14 rules
- **low**: 3 rules
- **medium**: 181 rules

## Usage

```hcl
module "cmmc_lvl2_macos_14" {
  source = "./modules/compliance/cmmc_lvl2/macos_14"

  enforcement_mode = "MONITOR_AND_ENFORCE"

  # Override organization-defined values
  rule_overrides = {
    "example_rule_id" = {
      odv_value = "your-value-here"
    }
  }

  # Exempt rules with justification
  exemptions = {
    "example_rule_id" = {
      reason      = "Operational requirement"
      ticket      = "SEC-XXXX"
      risk_status = "ACCEPTED"
    }
  }
}
```

## Important

This module is **auto-generated** by `scripts/generate_tf_compliance.py`.
Do not edit files in this directory directly — changes will be overwritten
on the next CI run.

To add or remove rules, modify the generator script or update the upstream
mSCP baseline definition at https://github.com/usnistgov/macos_security.

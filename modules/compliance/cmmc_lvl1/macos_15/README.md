# CMMC 2.0 — Level 1 — macOS 15

## Overview

- **Baseline key**: `cmmc_lvl1`
- **Category**: government
- **macOS version**: 15 (15.0+)
- **mSCP branch**: `sequoia`
- **mSCP revision**: `rev4.0`
- **Rule count**: 86

## Severity distribution

- **high**: 7 rules
- **medium**: 79 rules

## Usage

```hcl
module "cmmc_lvl1_macos_15" {
  source = "./modules/compliance/cmmc_lvl1/macos_15"

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

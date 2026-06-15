# CNSSI 1253 — High — macOS 15

## Overview

- **Baseline key**: `cnssi-1253_high`
- **Category**: government
- **macOS version**: 15 (15.0+)
- **mSCP branch**: `sequoia`
- **mSCP revision**: `rev4.0`
- **Rule count**: 265

## Severity distribution

- **high**: 14 rules
- **low**: 5 rules
- **medium**: 246 rules

## Usage

```hcl
module "cnssi-1253_high_macos_15" {
  source = "./modules/compliance/cnssi-1253_high/macos_15"

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

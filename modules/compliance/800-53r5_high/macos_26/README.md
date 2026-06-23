# NIST SP 800-53 Rev 5 — High — macOS 26

## Overview

- **Baseline key**: `800-53r5_high`
- **Category**: government
- **macOS version**: 26 (26.0+)
- **mSCP branch**: `tahoe`
- **mSCP revision**: `rev3.0`
- **Rule count**: 217

## Severity distribution

- **high**: 14 rules
- **low**: 2 rules
- **medium**: 201 rules

## Usage

```hcl
module "800-53r5_high_macos_26" {
  source = "./modules/compliance/800-53r5_high/macos_26"

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

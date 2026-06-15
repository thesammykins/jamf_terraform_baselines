---
name: manage-exemptions
description: Guide for declaring, reviewing, and maintaining security control exemptions with audit trails. Triggers on "exemption", "exclude rule", "waive control", "risk acceptance", "compensating control".
---

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

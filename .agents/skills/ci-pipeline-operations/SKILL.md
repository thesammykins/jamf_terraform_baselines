---
name: ci-pipeline-operations
description: Guide for operating the CI pipeline — triggering, monitoring, and troubleshooting compliance and foundation update pipelines. Triggers on "compliance update", "trigger CI", "check mSCP releases", "pipeline status", "force regeneration".
---

# CI Pipeline Operations

Operate the automated compliance baseline and foundation update pipelines.

## Scheduled behavior

- **Compliance update**: Weekly Monday 06:00 UTC. Polls mSCP releases. Opens PR if new revisions found.
- **Foundation update**: Monthly first Monday 06:00 UTC. Checks for PPPC bundle ID updates and provider version bumps.
- **Exemption check**: Every push and PR. Validates exemption expiration and completeness.

## Manual triggers

### Trigger compliance check on-demand

```bash
gh workflow run compliance-update.yml \
  --ref main \
  -f mscp_branch=tahoe
```

Omit `mscp_branch` or set to `all` to check all branches.

### Force regeneration for a specific branch

```bash
gh workflow run compliance-update.yml \
  --ref main \
  -f mscp_branch=sequoia
```

This re-generates even if no new release is detected (useful for testing generator changes).

### Trigger foundation update

```bash
gh workflow run foundation-update.yml --ref main
```

## Checking pipeline status

```bash
gh run list --workflow=compliance-update.yml --limit 5
gh run view {run_id}
```

## Troubleshooting

### Generator fails

1. Check if mSCP repo is accessible:
   ```bash
   gh api repos/usnistgov/macos_security/releases/latest
   ```

2. Check if mSCP container image is available:
   ```bash
   docker pull ghcr.io/usnistgov/mscp_2.0:latest
   ```

3. Run generator locally to reproduce:
   ```bash
   git clone -b tahoe https://github.com/usnistgov/macos_security.git /tmp/mscp
   python scripts/generate_tf_compliance.py \
     --mscp-path /tmp/mscp \
     --output /tmp/test-output \
     --branch tahoe
   ```

### Terraform validate fails on generated module

1. Check if the Jamf Platform provider schema changed:
   ```bash
   terraform providers schema -json | jq '.provider_schemas["registry.terraform.io/Jamf-Concepts/jamfplatform"]'
   ```

2. Compare against the generated resource shape in TECH.md.

### Exemption check blocks PR

1. Read the CI log for the specific exemption that failed.
2. Either:
   - Remove the expired exemption and enable the rule, OR
   - Extend the `expires` date with updated justification, OR
   - Change `risk_status` to `ACCEPTED` if it should be permanent.

### Multiple compliance PRs open simultaneously

This happens when multiple mSCP branches release simultaneously. Review and merge each PR independently. They target different module directories and won't conflict.

## Anti-patterns

1. **Merging compliance PRs without reviewing the changelog**: New rules may conflict with existing exemptions.
2. **Force-regenerating in production**: Test locally first with `--output /tmp/test-output`.
3. **Ignoring exemption check failures**: Expired TEMPORARY exemptions are a real compliance gap.

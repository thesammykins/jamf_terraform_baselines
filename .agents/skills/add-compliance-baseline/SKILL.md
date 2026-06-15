---
name: add-compliance-baseline
description: Guide for extending the pipeline to support a new NIST mSCP baseline or macOS version. Triggers on "add baseline", "new compliance framework", "add mSCP baseline", "new benchmark".
---

# Adding a Compliance Baseline

Extend the pipeline to support a new mSCP baseline or macOS version.

## Adding a new baseline

When NIST mSCP adds a new baseline (e.g., a new framework or country-specific baseline):

1. Verify the baseline exists in the mSCP repo:
   ```bash
   git clone -b tahoe https://github.com/usnistgov/macos_security.git /tmp/mscp
   ls /tmp/mscp/baselines/
   ```

2. Add the baseline key to the generator config:
   ```python
   # scripts/generate_tf_compliance.py
   SUPPORTED_BASELINES = {
       # ... existing baselines ...
       "new_baseline_key": {
           "display_name": "New Framework Display Name",
           "category": "government",  # government | industry | international
       }
   }
   ```

3. Run the generator locally to produce baseline modules:
   ```bash
   python scripts/generate_tf_compliance.py \
     --mscp-path /tmp/mscp \
     --output modules/compliance \
     --baseline new_baseline_key
   ```

4. Verify generated modules:
   ```bash
   for dir in modules/compliance/new_baseline_key/macos_*/; do
     (cd "$dir" && terraform init -backend=false && terraform validate)
   done
   ```

5. Add an example to `examples/compliance-only/main.tf`

6. Open PR with baseline description and rule count

## Adding a new macOS version

When Apple releases a new macOS and mSCP creates a corresponding branch:

1. Add the version to the supported list:
   ```python
   # scripts/generate_tf_compliance.py
   SUPPORTED_VERSIONS = {
       "14": {"name": "Sonoma", "min": "14.0", "branch": "sonoma"},
       "15": {"name": "Sequoia", "min": "15.0", "branch": "sequoia"},
       "26": {"name": "Tahoe", "min": "26.0", "branch": "tahoe"},
       "27": {"name": "NewOS", "min": "27.0", "branch": "newos_branch"},
   }
   ```

2. Run the generator for all baselines against the new version:
   ```bash
   python scripts/generate_tf_compliance.py \
     --mscp-path /tmp/mscp \
     --output modules/compliance \
     --version 27
   ```

3. Update the Foundation `os-version-smart-groups` module to include the new OS.

4. Verify and open PR.

## Adding custom rules to a baseline

1. Create a custom rule override in `modules/compliance/{baseline}/macos_{version}/overrides.tf`:
   ```hcl
   locals {
     custom_rules = {
       "my_org_custom_rule" = {
         title       = "My Org Custom Rule"
         description = "Additional control not in upstream mSCP"
         severity    = "medium"
       }
     }
   }
   ```

2. Reference in the benchmark's `rules` block.

3. Document the custom rule's purpose and NIST 800-53 mapping in a comment.

## Anti-patterns

1. **Adding a baseline without testing generation**: Always run `terraform validate` locally.
2. **Skipping the example**: Every new baseline needs a usage example so consumers can discover it.
3. **Hardcoding baseline lists in multiple places**: The generator config is the single source of truth.

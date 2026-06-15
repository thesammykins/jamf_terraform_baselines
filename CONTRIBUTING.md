# Contributing

## Scope

This repository contains two sets of Terraform modules:
- **Compliance modules** (`modules/compliance/`) — auto-generated from NIST mSCP baselines
- **Foundation modules** (`modules/foundation/`) — hand-authored Jamf Pro scaffolding

## Before you contribute

1. Check existing issues and PRs for duplicates
2. For compliance modules: changes to generated code should go into the generator (`scripts/generate_tf_compliance.py`), not into generated files directly
3. For foundation modules: changes are welcome but should follow existing patterns

## Development setup

```bash
# Clone with specs
git clone https://github.com/your-org/jamf_mscp_tf.git
cd jamf_mscp_tf

# Install Python dependencies for generator scripts
python3 -m venv .venv
source .venv/bin/activate
pip install pyyaml jinja2

# Install Terraform
brew install terraform  # or via mise: mise install terraform
```

## Making changes

### Compliance module changes

1. Modify `scripts/generate_tf_compliance.py`
2. Run locally: `python scripts/generate_tf_compliance.py --mscp-path /path/to/mscp --output /tmp/test`
3. Verify: `terraform validate` on generated output
4. Write/update unit tests in `tests/`
5. Open PR with before/after example of generated output

### Foundation module changes

1. Modify the module directly in `modules/foundation/{module}/`
2. Update `examples/foundation-only/main.tf` if the interface changes
3. Run `terraform fmt -recursive` and `terraform validate`
4. Test against a Jamf Pro staging instance
5. Open PR

### Adding a skill

1. Create `.agents/skills/{skill-name}/SKILL.md`
2. Follow the existing skill format (PHASE-based, with anti-patterns)
3. Reference the skill in `AGENTS.md`
4. Open PR

## PR requirements

- PR title follows conventional commits: `compliance:`, `foundation:`, `ci:`, `docs:`, `spec:`
- Generated compliance PRs are exempt from the conventional title requirement (they use `compliance:` automatically)
- All changes pass `terraform fmt -check -recursive` and `terraform validate`
- Exemption check CI passes
- At least one review from a CODEOWNER

## Testing

```bash
# Python unit tests
pytest tests/

# Terraform validation (all modules)
for dir in modules/compliance/*/macos_*/ modules/foundation/*/; do
  (cd "$dir" && terraform init -backend=false && terraform validate)
done

# Exemption check
python scripts/check_exemptions.py --modules-dir modules/ --enforce-expiry false
```

## Code Style

### HCL/Terraform
- `terraform fmt` is the authority
- Use `_` for resource names (not `-`)
- Variables: lowercase with underscores
- Outputs: include `description`
- Comments: explain *why*, not *what*

### Python
- Type hints on all function signatures
- Docstrings for public functions
- ruff for linting/formatting

### YAML (skills, configs)
- 2-space indent
- Comments above complex blocks, not inline

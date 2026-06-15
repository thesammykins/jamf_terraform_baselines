# Migrating existing Jamf Pro configs to Terraform

If you already manage a Jamf Pro tenant through the web UI or API scripting, this guide helps you bring those configurations under Terraform without breaking anything.

## Strategy: layer, don't replace

The safest approach is to add these Terraform modules **alongside** your existing configs, then gradually adopt resources:

1. Deploy foundation modules in a dry-run (`terraform plan` only)
2. Compare what Terraform would create against what you already have
3. Import matching resources so Terraform manages them instead of recreating them
4. Add compliance baselines — these generally don't conflict with existing profiles
5. Phase out manually-managed configs as Terraform takes over

## Step 1: Set up Terraform with a remote state backend

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket = "your-terraform-state-bucket"
    key    = "jamf-prod/terraform.tfstate"
    region = "us-east-1"
  }
}
```

Or use Terraform Cloud, Azure storage, or GCS. The important thing: don't use local state for anything you plan to keep.

Alternatively, start with local state during initial exploration and migrate to a remote backend later.

## Step 2: Auth and plan — no changes yet

Set your Jamf Pro credentials (see the [main README](../README.md#authentication)) and run:

```bash
terraform init
terraform plan -out=plan.tfplan
```

Review the plan. It will show every new resource Terraform *would* create. This is your inventory — if anything in the plan already exists in Jamf Pro, you'll want to import it.

## Step 3: Import existing resources

If you already have configuration profiles, categories, or smart groups that overlap with what these modules create, import them:

```bash
# Import an existing configuration profile
terraform import 'module.security_baseline.jamfpro_macos_configuration_profile_plist.filevault[0]' 123

# Import an existing category
terraform import 'module.categories.jamfpro_category.default["Security"]' 456
```

The resource address (first argument) comes from the module's resources. Look at each module's `main.tf` to find the exact resource names. The ID (second argument) is the Jamf Pro object ID — find it in the Jamf Pro URL when viewing the object (e.g., `https://your-org.jamfcloud.com/configurationProfiles.html?id=123`).

**Important**: import one resource at a time, then run `terraform plan` to verify Terraform sees it as managed rather than something to create.

## Step 4: Let Terraform reconcile the plan

After importing, run `terraform plan` again:

```bash
terraform plan
```

Terraform will now show only *differences* between your imported resources and the module definitions. If the plan is clean (no changes), you're in sync. If it shows changes, review them — they may be drift you want to accept, or configuration mismatches you need to fix.

## Step 5: Apply once the plan is clean

```bash
terraform apply
```

## Handling naming conflicts

These modules name resources with predictable patterns (e.g., `"Security Baseline — FileVault"`). If you already have a profile with that exact name, Terraform will try to create a duplicate and Jamf Pro will reject it.

Options:
- **Option A: Rename the existing profile** in Jamf Pro, then import it under the module's expected name.
- **Option B: Let Terraform create a new one**, then manually delete the old one after verifying the new one works.
- **Option C: Don't use that module** — write your own `terraform import` block for the existing resource and manage it directly.

Foundation modules are designed to be individually enabled/disabled, so you can skip any module that conflicts with existing configs you want to keep as-is.

## Pattern: export → map → import

For bulk migration, follow this pattern:

1. **Export** your existing Jamf Pro configuration as JSON using the Jamf Pro API or Classic API.
2. **Map** each JSON object to the Terraform resource type it corresponds to:
   - Configuration profiles → `jamfpro_macos_configuration_profile_plist`
   - Categories → `jamfpro_category`
   - Smart groups → `jamfpro_smart_computer_group`
   - Policies → `jamfpro_policy`
3. **Import** each resource by ID into a Terraform block.
4. **Compare** the imported resource attributes against the module's expected values. Adjust variables or accept drift.

## Foundation modules and existing tenants

Foundation modules are designed to co-exist with existing Jamf Pro configurations. They don't take over your entire tenant — they create specific, well-scoped resources:

| Module | Will it conflict with existing configs? | What to watch for |
|---|---|---|
| `categories` | Only if you already have categories named `Security`, `Productivity`, etc. | The module creates standard categories. If yours differ, skip this module. |
| `os-version-smart-groups` | Unlikely unless you have identically-named smart groups | Smart group names include the macOS version. |
| `security-baseline` | Possibly — if you already have FileVault/firewall/Gatekeeper profiles | Import existing profiles first. |
| `software-updates` | Possibly — if you have existing software update policies | Import or keep your existing and skip this module. |
| `pppc-screen-capture` | Unlikely — PPPC profiles can coexist | Multiple PPPC profiles for the same apps are fine. |
| `pppc-accessibility` | Unlikely | Same as above. |
| `device-enrollment` | Maybe — if you have existing PreStage enrollments | PreStage names must be unique. |
| `inventory-settings` | Unlikely — these are Jamf Pro server-level settings | Only one inventory collection configuration exists. |

## Compliance baselines and existing tenants

Compliance modules create Jamf Platform Compliance Benchmark Engine resources. These reference the Jamf Platform API, not Jamf Pro directly, so they generally don't conflict with existing Jamf Pro configuration profiles. You can deploy them alongside anything you already have.

## Getting help

- Check the [full-stack example](../examples/full-stack/) for a complete working configuration
- Read the [PRODUCT.md spec](../specs/mscp-terraform-pipeline/PRODUCT.md) for detailed behavior descriptions
- Open an issue on the repository with your specific scenario

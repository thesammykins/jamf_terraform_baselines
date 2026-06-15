# Categories module — creates standard Jamf Pro categories for the macAdmin Foundation.
# These categories are used by policies and profiles for organization.

locals {
  category_names = [
    "Security",
    "Productivity",
    "Utilities",
    "Communication",
    "Browsers",
    "Developer Tools",
  ]
}

resource "jamfpro_category" "this" {
  count = (
    var.enable_categories &&
    !contains(keys(var.exemptions), "categories")
  ) ? length(local.category_names) : 0

  name     = local.category_names[count.index]
  priority = count.index
}

output "category_ids" {
  value = {
    for i, cat in jamfpro_category.this :
    cat.name => cat.id
  }
  description = "Map of category names to their Jamf Pro IDs"
}


output "exemptions" {
  value = {
    for k, v in var.exemptions : k => merge(v, {
      module    = var.module_name
      timestamp = timestamp()
    })
  }
  description = "Active exemptions with audit justification"
}

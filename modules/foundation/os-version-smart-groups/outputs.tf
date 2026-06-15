output "smart_group_ids" {
  value = {
    for i, group in jamfpro_smart_computer_group_v2.this :
    group.name => group.id
  }
  description = "Map of smart group names to their Jamf Pro IDs"
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

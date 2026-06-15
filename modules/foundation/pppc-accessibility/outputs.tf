output "profile_id" {
  value       = one(jamfpro_macos_configuration_profile_plist.pppc_accessibility[*].id)
  description = "Jamf Pro ID of the PPPC accessibility configuration profile"
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

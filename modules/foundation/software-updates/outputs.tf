output "feature_toggle_id" {
  value       = one(jamfpro_managed_software_update_feature_toggle.enable[*].id)
  description = "Jamf Pro ID of the Managed Software Update feature toggle"
}

output "ddm_plan_ids" {
  value = {
    for k, v in jamfpro_managed_software_update.ddm_plans : k => v.id
  }
  description = "Map of smart group names to their DDM Managed Software Update plan IDs"
}

output "legacy_profile_id" {
  value       = one(jamfpro_macos_configuration_profile_plist.software_update_legacy[*].id)
  description = "Jamf Pro ID of the deprecated legacy software update configuration profile"
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

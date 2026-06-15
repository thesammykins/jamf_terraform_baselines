output "ddm_profile_id" {
  value       = one(jamfpro_macos_configuration_profile_plist.external_intelligence_ddm[*].id)
  description = "Jamf Pro ID of the DDM-native External Intelligence configuration profile"
}

output "legacy_profile_id" {
  value       = one(jamfpro_macos_configuration_profile_plist.external_intelligence_legacy[*].id)
  description = "Jamf Pro ID of the legacy External Intelligence configuration profile"
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

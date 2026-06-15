output "ddm_profile_id" {
  value       = one(jamfpro_macos_configuration_profile_plist.intelligence_ddm[*].id)
  description = "Jamf Pro ID of the DDM-native Apple Intelligence configuration profile"
}

output "legacy_profile_id" {
  value       = one(jamfpro_macos_configuration_profile_plist.intelligence_legacy[*].id)
  description = "Jamf Pro ID of the legacy Apple Intelligence configuration profile"
}

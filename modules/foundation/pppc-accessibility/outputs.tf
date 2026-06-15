output "profile_id" {
  value       = one(jamfpro_macos_configuration_profile_plist.pppc_accessibility[*].id)
  description = "Jamf Pro ID of the PPPC accessibility configuration profile"
}

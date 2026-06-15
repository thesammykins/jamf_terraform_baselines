output "profile_id" {
  value       = one(jamfpro_macos_configuration_profile_plist.software_update[*].id)
  description = "Jamf Pro ID of the software update configuration profile"
}

output "profile_id" {
  value       = one(jamfpro_macos_configuration_profile_plist.pppc_screen_capture[*].id)
  description = "Jamf Pro ID of the PPPC screen capture configuration profile"
}

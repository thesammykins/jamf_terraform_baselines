output "profile_ids" {
  value = {
    filevault   = one(jamfpro_macos_configuration_profile_plist.filevault[*].id)
    firewall    = one(jamfpro_macos_configuration_profile_plist.firewall[*].id)
    screensaver = one(jamfpro_macos_configuration_profile_plist.screensaver[*].id)
    gatekeeper  = one(jamfpro_macos_configuration_profile_plist.gatekeeper[*].id)
  }
  description = "Map of security baseline profile names to their Jamf Pro IDs"
}

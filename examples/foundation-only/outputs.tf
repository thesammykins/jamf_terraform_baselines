output "foundation_categories" {
  description = "IDs of created Jamf Pro categories (Security, Productivity, Utilities, Communication, Browsers, Developer Tools)"
  value       = module.foundation.categories
}

output "foundation_smart_groups" {
  description = "IDs of OS-version smart computer groups (macOS 14, 15, 26, Unsupported)"
  value       = module.foundation.smart_groups
}

output "foundation_security_profiles" {
  description = "IDs of deployed security baseline configuration profiles"
  value       = module.foundation.security_profiles
}

output "foundation_software_update_profiles" {
  description = "IDs of deployed software update configuration profiles"
  value       = module.foundation.software_update_profiles
}

output "foundation_pppc_profiles" {
  description = "IDs of deployed PPPC configuration profiles"
  value       = module.foundation.pppc_profiles
}

output "foundation_device_enrollment" {
  description = "ADE enrollment settings configured"
  value       = module.foundation.device_enrollment
}

output "foundation_inventory_settings" {
  description = "Jamf Pro inventory collection settings"
  value       = module.foundation.inventory_settings
}

output "foundation_exemptions" {
  description = "Active exemptions for foundation modules"
  value       = module.foundation.exemptions
}

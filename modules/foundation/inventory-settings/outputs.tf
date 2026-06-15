output "inventory_settings_id" {
  value       = one(jamfpro_computer_checkin.inventory_settings[*].id)
  description = "Jamf Pro ID of the computer check-in and inventory settings"
}

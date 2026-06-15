output "client_checkin_id" {
  value       = one(jamfpro_client_checkin.inventory_settings[*].id)
  description = "Jamf Pro ID of the client check-in settings"
}

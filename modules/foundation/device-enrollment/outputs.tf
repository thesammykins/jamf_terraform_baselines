output "enrollment_settings_id" {
  value       = one(jamfpro_enrollment_settings.device_enrollment[*].id)
  description = "Jamf Pro ID of the automated device enrollment settings"
}

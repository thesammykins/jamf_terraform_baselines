output "prestage_enrollment_id" {
  value       = one(jamfpro_computer_prestage_enrollment.device_enrollment[*].id)
  description = "Jamf Pro ID of the computer prestage enrollment"
}

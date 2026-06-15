output "prestage_enrollment_id" {
  value       = one(jamfpro_computer_prestage_enrollment.device_enrollment[*].id)
  description = "Jamf Pro ID of the computer prestage enrollment"
}


output "exemptions" {
  value = {
    for k, v in var.exemptions : k => merge(v, {
      module    = var.module_name
      timestamp = timestamp()
    })
  }
  description = "Active exemptions with audit justification"
}

output "client_checkin_id" {
  value       = one(jamfpro_client_checkin.inventory_settings[*].id)
  description = "Jamf Pro ID of the client check-in settings"
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

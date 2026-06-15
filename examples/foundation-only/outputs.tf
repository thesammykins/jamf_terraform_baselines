output "smart_group_ids" {
  description = "OS version smart group IDs for use in DDM update plan targeting"
  value       = module.os_version_smart_groups.smart_group_ids
}

output "security_profile_ids" {
  description = "Security baseline configuration profile IDs (filevault, firewall, screensaver, gatekeeper)"
  value       = module.security_baseline.profile_ids
}

output "software_update_ddm_plan_ids" {
  description = "DDM-native software update plan IDs per version group"
  value       = module.software_updates.ddm_plan_ids
}

output "software_update_feature_toggle_id" {
  description = "Managed Software Update feature toggle ID"
  value       = module.software_updates.feature_toggle_id
}

output "prestage_enrollment_id" {
  description = "Computer prestage enrollment ID"
  value       = module.device_enrollment.prestage_enrollment_id
}

output "client_checkin_id" {
  description = "Client check-in settings ID"
  value       = module.inventory_settings.client_checkin_id
}

output "intelligence_ddm_profile_id" {
  description = "DDM-native Apple Intelligence configuration profile ID"
  value       = module.intelligence_settings.ddm_profile_id
}

output "external_intelligence_ddm_profile_id" {
  description = "DDM-native External Intelligence configuration profile ID"
  value       = module.external_intelligence_settings.ddm_profile_id
}

output "cis_l1_tahoe_benchmark_id" {
  description = "ID of the CIS Level 1 compliance benchmark for macOS 26"
  value       = module.cis_l1_tahoe.benchmark_id
}

output "cis_l1_tahoe_device_group_id" {
  description = "ID of the smart device group targeting macOS 26 devices"
  value       = module.cis_l1_tahoe.device_group_id
}

output "cis_l1_tahoe_exemptions" {
  description = "Active exemptions for CIS Level 1 baseline on macOS 26"
  value       = module.cis_l1_tahoe.exemptions
}

output "disa_stig_tahoe_benchmark_id" {
  description = "ID of the DISA STIG compliance benchmark for macOS 26"
  value       = module.disa_stig_tahoe.benchmark_id
}

output "disa_stig_tahoe_device_group_id" {
  description = "ID of the smart device group targeting macOS 26 devices"
  value       = module.disa_stig_tahoe.device_group_id
}

output "disa_stig_tahoe_exemptions" {
  description = "Active exemptions for DISA STIG baseline on macOS 26"
  value       = module.disa_stig_tahoe.exemptions
}

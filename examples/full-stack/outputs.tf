# ── Variant A — Compliance Outputs ────────────────────────────────────

output "compliance_benchmarks" {
  description = "Summary of all deployed compliance benchmarks with IDs"
  value = {
    cis_l1_tahoe                 = module.cis_l1_tahoe.benchmark_id
    disa_stig_tahoe              = module.disa_stig_tahoe.benchmark_id
    nist_80053_moderate_tahoe    = module.nist_80053_moderate_tahoe.benchmark_id
  }
}

output "compliance_device_groups" {
  description = "Smart device groups created for compliance targeting"
  value = {
    cis_l1_tahoe                 = module.cis_l1_tahoe.device_group_id
    disa_stig_tahoe              = module.disa_stig_tahoe.device_group_id
    nist_80053_moderate_tahoe    = module.nist_80053_moderate_tahoe.device_group_id
  }
}

output "compliance_exemptions" {
  description = "All active exemptions across compliance baselines"
  value = merge(
    { for k, v in module.cis_l1_tahoe.exemptions : "cis_l1/${k}" => v },
    { for k, v in module.disa_stig_tahoe.exemptions : "disa_stig/${k}" => v },
    { for k, v in module.nist_80053_moderate_tahoe.exemptions : "800-53_moderate/${k}" => v },
  )
}

# ── Variant B — Foundation Outputs ────────────────────────────────────

output "foundation_summary" {
  description = "Summary of deployed macAdmin Foundation resources"
  value = {
    categories             = module.foundation.categories
    os_version_smart_groups = module.foundation.smart_groups
    security_profiles       = module.foundation.security_profiles
    software_update_profiles = module.foundation.software_update_profiles
    pppc_profiles           = module.foundation.pppc_profiles
    device_enrollment       = module.foundation.device_enrollment
    inventory_settings      = module.foundation.inventory_settings
  }
}

output "foundation_exemptions" {
  description = "Active exemptions for foundation modules"
  value       = module.foundation.exemptions
}

# ── Combined Exemption Report ─────────────────────────────────────────

output "all_exemptions" {
  description = "Complete exemption report for all variants (GRC-consumable)"
  value = merge(
    { for k, v in module.cis_l1_tahoe.exemptions : "compliance.cis_l1.${k}" => v },
    { for k, v in module.disa_stig_tahoe.exemptions : "compliance.disa_stig.${k}" => v },
    { for k, v in module.nist_80053_moderate_tahoe.exemptions : "compliance.800-53_moderate.${k}" => v },
    { for k, v in module.foundation.exemptions : "foundation.${k}" => v },
  )
}

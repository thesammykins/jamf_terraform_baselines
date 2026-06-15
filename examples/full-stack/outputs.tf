# ── Variant A — Compliance Outputs ────────────────────────────────────

output "compliance_benchmarks" {
  description = "Summary of all deployed compliance benchmarks with IDs"
  value = {
    cis_l1_tahoe              = module.cis_l1_tahoe.benchmark_id
    disa_stig_tahoe           = module.disa_stig_tahoe.benchmark_id
    nist_80053_moderate_tahoe = module.nist_80053_moderate_tahoe.benchmark_id
  }
}

output "compliance_device_groups" {
  description = "Smart device groups created for compliance targeting"
  value = {
    cis_l1_tahoe              = module.cis_l1_tahoe.device_group_id
    disa_stig_tahoe           = module.disa_stig_tahoe.device_group_id
    nist_80053_moderate_tahoe = module.nist_80053_moderate_tahoe.device_group_id
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
    smart_groups              = module.os_version_smart_groups.smart_group_ids
    security_profiles         = module.security_baseline.profile_ids
    software_update_ddm_plans = module.software_updates.ddm_plan_ids
    software_update_toggle    = module.software_updates.feature_toggle_id
    prestage_enrollment       = module.device_enrollment.prestage_enrollment_id
    client_checkin            = module.inventory_settings.client_checkin_id
    intelligence_ddm          = module.intelligence_settings.ddm_profile_id
    external_intelligence_ddm = module.external_intelligence_settings.ddm_profile_id
  }
}

output "foundation_exemptions" {
  description = "Active exemptions for foundation modules (exemptions are module inputs, not forwarded outputs)"
  value = {
    note = "Exemptions are configured per-module as input variables. See terraform.tfvars for exemption details."
  }
}

# ── Combined Exemption Report ─────────────────────────────────────────

output "all_exemptions" {
  description = "Complete exemption report for all variants (GRC-consumable)"
  value = merge(
    { for k, v in module.cis_l1_tahoe.exemptions : "compliance.cis_l1.${k}" => v },
    { for k, v in module.disa_stig_tahoe.exemptions : "compliance.disa_stig.${k}" => v },
    { for k, v in module.nist_80053_moderate_tahoe.exemptions : "compliance.800-53_moderate.${k}" => v },
  )
  # NOTE: Foundation modules don't expose exemptions as outputs.
  # Exemptions are module inputs configured via terraform.tfvars.
}

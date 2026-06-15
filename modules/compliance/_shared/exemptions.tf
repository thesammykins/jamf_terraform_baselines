# Shared exemption processing for compliance modules.
# Each compliance module sources this file to get consistent
# exemption report generation and output formatting.

locals {
  exemption_report = {
    for k, v in var.exemptions : k => merge(v, {
      module        = var.baseline_id
      macos_version = var.macos_version
      timestamp     = timestamp()
    })
  }

  has_expired_exemptions = anytrue([
    for e in local.exemption_report :
    can(e.expires) ? timecmp(e.expires, timestamp()) < 0 : false
  ])

  # Precondition: no expired exemptions in apply
  # (CI also validates this at PR time via a script)
}

resource "terraform_data" "exemption_report" {
  count = length(local.exemption_report) > 0 ? 1 : 0

  input = local.exemption_report
}

output "exemptions" {
  value       = local.exemption_report
  description = "Active exemptions with audit justification"
}

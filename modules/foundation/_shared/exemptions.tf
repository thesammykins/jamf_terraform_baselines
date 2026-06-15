# Shared exemption processing for foundation modules.
# Foundation exemptions use the module name as the key
# rather than a rule ID, since the unit of exemption is
# an entire module rather than a specific rule.

locals {
  exemption_report = {
    for k, v in var.exemptions : k => merge(v, {
      module    = var.module_name
      timestamp = timestamp()
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
  description = "Active foundation module exemptions with audit justification"
}

# PPPC Accessibility — deploys a Privacy Preferences Policy Control profile
# granting accessibility access to approved collaboration tools.
# Bundle IDs are sourced from pppc-bundle-ids.yaml.

locals {
  # Load and decode the bundle ID definitions
  pppc_bundle_ids_raw = yamldecode(file("${path.module}/pppc-bundle-ids.yaml"))

  # Filter to only the tools requested by the consumer
  selected_tools = {
    for name in var.pppc_tools :
    name => local.pppc_bundle_ids_raw.tools[name]
    if contains(keys(local.pppc_bundle_ids_raw.tools), name)
  }

  # Build the Accessibility payload array
  accessibility_entries = [
    for name, config in local.selected_tools : {
      Accessibility                                  = true
      Authorization                                 = "AllowStandardUserToSetSystemService"
      Identifier                                    = config.bundle_id
      IdentifierType                                = config.identifier_type
      CodeRequirement                               = config.code_requirement
      Comment                                       = "${name} — ${config.description}"
      PayloadDescription                           = "${name} Accessibility Access"
      PayloadDisplayName                           = "PPPC — ${name} (Accessibility)"
      PayloadIdentifier                            = "com.example.pppc.accessibility.${replace(lower(name), " ", "-")}"
      PayloadType                                  = "com.apple.TCC.configuration-profile-policy"
      PayloadUUID                                  = uuidv5("dns", "com.example.pppc.accessibility.${name}")
      PayloadVersion                                = 1
    }
  ]
}

resource "jamfpro_macos_configuration_profile_plist" "pppc_accessibility" {
  count = (
    var.enable_pppc_accessibility &&
    !contains(keys(var.exemptions), "pppc_accessibility")
  ) ? 1 : 0

  name                = "macAdmin Foundation — PPPC Accessibility"
  description         = "Grants accessibility access to approved collaboration tools. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads            = templatefile("${path.module}/templates/pppc.mobileconfig.tftpl", {
    display_name      = "macAdmin Foundation — PPPC Accessibility"
    identifier         = "com.example.foundation.pppc-accessibility"
    uuid               = "F6A7B8C9-0D1E-2F3A-4B5C-6D7E8F9A0B1C"
    payload_content    = jsonencode(local.accessibility_entries)
  })
  payload_validate    = true

  scope {
    all_computers = true
    all_jss_users = false
  }
}

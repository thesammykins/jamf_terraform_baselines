# PPPC Screen Capture — deploys a Privacy Preferences Policy Control profile
# granting screen capture access to approved collaboration tools.
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

  # Build the ScreenCapture payload array
  screen_capture_entries = [
    for name, config in local.selected_tools : {
      AllowScreenCapture                            = true
      Authorization                                 = "AllowStandardUserToSetSystemService"
      Identifier                                    = config.bundle_id
      IdentifierType                                = config.identifier_type
      CodeRequirement                               = config.code_requirement
      Comment                                       = "${name} — ${config.description}"
      PayloadDescription                           = "${name} Screen Capture Access"
      PayloadDisplayName                           = "PPPC — ${name} (Screen Capture)"
      PayloadIdentifier                            = "com.example.pppc.screen-capture.${replace(lower(name), " ", "-")}"
      PayloadType                                  = "com.apple.TCC.configuration-profile-policy"
      PayloadUUID                                  = uuidv5("dns", "com.example.pppc.screen-capture.${name}")
      PayloadVersion                                = 1
    }
  ]
}

resource "jamfpro_macos_configuration_profile_plist" "pppc_screen_capture" {
  count = (
    var.enable_pppc_screen_capture &&
    !contains(keys(var.exemptions), "pppc_screen_capture")
  ) ? 1 : 0

  name                = "macAdmin Foundation — PPPC Screen Capture"
  description         = "Grants screen capture access to approved collaboration tools. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads            = templatefile("${path.module}/templates/pppc.mobileconfig.tftpl", {
    display_name      = "macAdmin Foundation — PPPC Screen Capture"
    identifier         = "com.example.foundation.pppc-screen-capture"
    uuid               = "E5F6A7B8-9C0D-1E2F-3A4B-5C6D7E8F9A0B"
    payload_content    = jsonencode(local.screen_capture_entries)
  })
  payload_validate    = true

  scope {
    all_computers = true
    all_jss_users = false
  }
}

# Inventory Settings — configures Jamf Pro client check-in frequency,
# startup scripts, and login/logout hook behaviors.

resource "jamfpro_client_checkin" "inventory_settings" {
  count = (
    var.enable_inventory_settings &&
    !contains(keys(var.exemptions), "inventory_settings")
  ) ? 1 : 0

  check_in_frequency                  = var.checkin_frequency_minutes
  create_startup_script               = true
  startup_log                         = true
  startup_ssh                         = false
  startup_policies                    = true
  create_hooks                        = false
  enable_local_configuration_profiles = true
  allow_network_state_change_triggers = true
}

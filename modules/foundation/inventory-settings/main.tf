# Inventory Settings — configures Jamf Pro computer check-in frequency,
# software update collection, and extension attribute collection settings.

resource "jamfpro_computer_checkin" "inventory_settings" {
  count = (
    var.enable_inventory_settings &&
    !contains(keys(var.exemptions), "inventory_settings")
  ) ? 1 : 0

  checkin_frequency_minutes = var.checkin_frequency_minutes

  # Collect software update information during check-in
  collect_software_updates = true

  # Collect extension attribute data during check-in
  collect_extension_attributes = true
}

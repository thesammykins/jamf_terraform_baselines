## Rule Changes — NIST SP 800-53 Rev 5 — High (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_configure_capacity_notify | Configure Audit Capacity Warning |
| ADDED | audit_failure_halt | Configure System to Shut Down Upon Audit Failure |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fd_configure | Configure System to Audit All Deletions of Object Attributes |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_record_reduction_report_generation | Audit Record Reduction and Report Generation |
| ADDED | audit_records_processing | Audit Record Reduction and Report Generation |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | audit_settings_failure_notify | Configure Audit Failure Notification |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_certificate_trust_enforce_high | Set Smartcard Certificate Trust to High |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_application_sandboxing | Ensure Separate Execution Domain for Processes |
| ADDED | os_asl_log_files_owner_group_configure | Configure Apple System Log Files Owned by Root and Group to Wheel |
| ADDED | os_asl_log_files_permissions_configure | Configure Apple System Log Files To Mode 640 or Less Permissive |
| ADDED | os_auth_peripherals | Must Authenticate Before Establishing a Connection |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_certificate_authority_trust | Issue or Obtain Public Key Certificates from an Approved Service Provider |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_config_profile_ui_install_disable | Disable Installation of Configuration Profiles through the User Interface |
| ADDED | os_continuous_monitoring | Configure Automated Flaw Remediation |
| ADDED | os_crypto_audit | Protect Audit Integrity with Cryptographic Mechanisms |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_enforce_access_restrictions | Enforce Access Restrictions |
| ADDED | os_external_storage_access_defined | Access to External Storage Must Be Defined |
| ADDED | os_fail_secure_state | Configure System to Fail to a Known Safe State if System Initialization, Shutdown, or Abort Fails |
| ADDED | os_filevault_authorized_users | FileVault Authorized Users |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_firewall_default_deny_require | Control Connections to Other Systems via a Deny-All and Allow-by-Exception Firewall Policy |
| ADDED | os_firmware_password_require | Enable Firmware Password |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_identify_non-org_users | Configure the System to Uniquely Identify and Authenticate Non-Organizational Users |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_implement_cryptography | Configure the System to Implement Approved Cryptography to Protect Information |
| ADDED | os_implement_memory_protection | Configure the System to Protect Memory from Unauthorized Code Execution |
| ADDED | os_information_validation | Information Input Validation |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_isolate_security_functions | Configure the System to Separate User and System Functionality |
| ADDED | os_limit_gui_sessions | Limit Concurrent GUI Sessions to 10 for all Accounts |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_loginwindow_adminhostinfo_disabled | Prevent AdminHostInfo from Being Available at Login Window |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_managed_access_control_points | Managed Access Control Points |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_newsyslog_files_owner_group_configure | Configure System Log Files Owned by Root and Group to Wheel |
| ADDED | os_newsyslog_files_permissions_configure | Configure System Log Files to Mode 640 or Less Permissive |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_non_repudiation | Non-Repudiation |
| ADDED | os_nonlocal_maintenance | Configure the System for Non-local Maintenance |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_policy_banner_ssh_configure | Display Policy Banner at Remote Login |
| ADDED | os_policy_banner_ssh_enforce | Enforce SSH to Display Policy Banner |
| ADDED | os_prevent_priv_functions | Configure the System to Block Non-Privileged Users from Executing Privileged Functions |
| ADDED | os_prevent_unauthorized_disclosure | Configure the System to Prevent the Unauthorized Disclosure of Data via Shared Resources |
| ADDED | os_prohibit_remote_activation_collab_devices | Prohibit Remote Activation of Collaborative Computing Devices |
| ADDED | os_protect_dos_attacks | Protect Against Denial of Service Attacks by Ensuring Rate-Limiting Measures on Network Interfaces |
| ADDED | os_provide_automated_account_management | Employ Automated Mechanisms for Account Management Functions |
| ADDED | os_reauth_devices_change_authenticators | Require Devices to Reauthenticate when Changing Authenticators |
| ADDED | os_reauth_users_change_authenticators | Require users to reauthenticate when changing authenticators |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_required_crypto_module | Ensure all Federal Laws, Executive Orders, Directives, Policies, Regulations, Standards, and Guidance for Authentication to a Cryptographic Module are Met |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_allow_javascript_disable | Disable JavaScript in Safari |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_screensaver_loginwindow_enforce | Enforce Screen Saver at Login Window |
| ADDED | os_secure_boot_verify | Ensure Secure Boot Level Set to Full |
| ADDED | os_secure_name_resolution | Secure Name Address Resolution Service |
| ADDED | os_separate_functionality | Configure the System to Separate User and System Functionality |
| ADDED | os_setup_assistant_filevault_enforce | Enforce FileVault in Setup Assistant |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_ssh_server_alive_count_max_configure | Set SSH Active Server Alive Maximum to $ODV |
| ADDED | os_ssh_server_alive_interval_configure | Configure SSH ServerAliveInterval option set to $ODV |
| ADDED | os_sshd_channel_timeout_configure | Configure SSHD Channel Timeout to $ODV |
| ADDED | os_sshd_client_alive_count_max_configure | Configure SSHD ClientAliveCountMax to $ODV |
| ADDED | os_sshd_client_alive_interval_configure | Configure SSHD ClientAliveInterval to $ODV |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_per_source_penalties_configure | Configure SSHD PerSourcePenalties |
| ADDED | os_sshd_permit_root_login_configure | Disable Root Login for SSH |
| ADDED | os_sshd_unused_connection_timeout_configure | Configure SSHD Unused Connection Timeout to $ODV |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudo_timeout_configure | Configure Sudo Timeout Period to $ODV |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_system_read_only | Ensure System Volume is Read Only |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unique_identification | Uniquely Identify Users and Processes |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_inactivity_enforce | Disable Accounts after $ODV Days of Inactivity |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_emergency_accounts_disable | Automatically Remove or Disable Emergency Accounts within 72 Hours |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | pwpolicy_temporary_accounts_disable | Automatically Remove or Disable Temporary User Accounts within 72 Hours |
| ADDED | pwpolicy_temporary_or_emergency_accounts_disable | Automatically Remove or Disable Temporary or Emergency User Accounts within 72 Hours |
| ADDED | supplemental_controls | Out of Scope Supplemental |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_firewall_pf | Packet Filter (pf) Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | supplemental_smartcard | Smartcard Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_apple_watch_unlock_disable | Prevent Apple Watch from Terminating a Session Lock |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_automatic_logout_enforce | Enforce Auto Logout After $ODV Seconds of Inactivity |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_disable | Disable Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_token_removal_enforce | Configure User Session Lock When a Smart Token is Removed |
| ADDED | system_settings_touch_id_settings_disable | Disable the Touch ID System Settings Pane |
| ADDED | system_settings_touchid_unlock_disable | Disable TouchID for Unlocking the Device |
| ADDED | system_settings_usb_restricted_mode | USB Devices Must be Authorized Before Allowing |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |
| ADDED | system_settings_wifi_disable | Disable Wi-Fi Interface |
| ADDED | system_settings_wifi_disable_when_connected_to_ethernet | Disable Wi-Fi When Connected to Ethernet |

## Rule Changes — NIST SP 800-53 Rev 5 — Moderate (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_failure_halt | Configure System to Shut Down Upon Audit Failure |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fd_configure | Configure System to Audit All Deletions of Object Attributes |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_record_reduction_report_generation | Audit Record Reduction and Report Generation |
| ADDED | audit_records_processing | Audit Record Reduction and Report Generation |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | audit_settings_failure_notify | Configure Audit Failure Notification |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_certificate_trust_enforce_moderate | Set Smartcard Certificate Trust to Moderate |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_application_sandboxing | Ensure Separate Execution Domain for Processes |
| ADDED | os_asl_log_files_owner_group_configure | Configure Apple System Log Files Owned by Root and Group to Wheel |
| ADDED | os_asl_log_files_permissions_configure | Configure Apple System Log Files To Mode 640 or Less Permissive |
| ADDED | os_auth_peripherals | Must Authenticate Before Establishing a Connection |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_certificate_authority_trust | Issue or Obtain Public Key Certificates from an Approved Service Provider |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_config_profile_ui_install_disable | Disable Installation of Configuration Profiles through the User Interface |
| ADDED | os_continuous_monitoring | Configure Automated Flaw Remediation |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_external_storage_access_defined | Access to External Storage Must Be Defined |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_firewall_default_deny_require | Control Connections to Other Systems via a Deny-All and Allow-by-Exception Firewall Policy |
| ADDED | os_firmware_password_require | Enable Firmware Password |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_identify_non-org_users | Configure the System to Uniquely Identify and Authenticate Non-Organizational Users |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_implement_cryptography | Configure the System to Implement Approved Cryptography to Protect Information |
| ADDED | os_implement_memory_protection | Configure the System to Protect Memory from Unauthorized Code Execution |
| ADDED | os_information_validation | Information Input Validation |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_loginwindow_adminhostinfo_disabled | Prevent AdminHostInfo from Being Available at Login Window |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_managed_access_control_points | Managed Access Control Points |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_newsyslog_files_owner_group_configure | Configure System Log Files Owned by Root and Group to Wheel |
| ADDED | os_newsyslog_files_permissions_configure | Configure System Log Files to Mode 640 or Less Permissive |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_nonlocal_maintenance | Configure the System for Non-local Maintenance |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_policy_banner_ssh_configure | Display Policy Banner at Remote Login |
| ADDED | os_policy_banner_ssh_enforce | Enforce SSH to Display Policy Banner |
| ADDED | os_prevent_priv_functions | Configure the System to Block Non-Privileged Users from Executing Privileged Functions |
| ADDED | os_prevent_unauthorized_disclosure | Configure the System to Prevent the Unauthorized Disclosure of Data via Shared Resources |
| ADDED | os_prohibit_remote_activation_collab_devices | Prohibit Remote Activation of Collaborative Computing Devices |
| ADDED | os_protect_dos_attacks | Protect Against Denial of Service Attacks by Ensuring Rate-Limiting Measures on Network Interfaces |
| ADDED | os_provide_automated_account_management | Employ Automated Mechanisms for Account Management Functions |
| ADDED | os_reauth_devices_change_authenticators | Require Devices to Reauthenticate when Changing Authenticators |
| ADDED | os_reauth_users_change_authenticators | Require users to reauthenticate when changing authenticators |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_required_crypto_module | Ensure all Federal Laws, Executive Orders, Directives, Policies, Regulations, Standards, and Guidance for Authentication to a Cryptographic Module are Met |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_allow_javascript_disable | Disable JavaScript in Safari |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_screensaver_loginwindow_enforce | Enforce Screen Saver at Login Window |
| ADDED | os_secure_boot_verify | Ensure Secure Boot Level Set to Full |
| ADDED | os_secure_name_resolution | Secure Name Address Resolution Service |
| ADDED | os_separate_functionality | Configure the System to Separate User and System Functionality |
| ADDED | os_setup_assistant_filevault_enforce | Enforce FileVault in Setup Assistant |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_ssh_server_alive_count_max_configure | Set SSH Active Server Alive Maximum to $ODV |
| ADDED | os_ssh_server_alive_interval_configure | Configure SSH ServerAliveInterval option set to $ODV |
| ADDED | os_sshd_channel_timeout_configure | Configure SSHD Channel Timeout to $ODV |
| ADDED | os_sshd_client_alive_count_max_configure | Configure SSHD ClientAliveCountMax to $ODV |
| ADDED | os_sshd_client_alive_interval_configure | Configure SSHD ClientAliveInterval to $ODV |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_per_source_penalties_configure | Configure SSHD PerSourcePenalties |
| ADDED | os_sshd_unused_connection_timeout_configure | Configure SSHD Unused Connection Timeout to $ODV |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudo_timeout_configure | Configure Sudo Timeout Period to $ODV |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_system_read_only | Ensure System Volume is Read Only |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unique_identification | Uniquely Identify Users and Processes |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_inactivity_enforce | Disable Accounts after $ODV Days of Inactivity |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_emergency_accounts_disable | Automatically Remove or Disable Emergency Accounts within 72 Hours |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | pwpolicy_temporary_accounts_disable | Automatically Remove or Disable Temporary User Accounts within 72 Hours |
| ADDED | pwpolicy_temporary_or_emergency_accounts_disable | Automatically Remove or Disable Temporary or Emergency User Accounts within 72 Hours |
| ADDED | supplemental_controls | Out of Scope Supplemental |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_firewall_pf | Packet Filter (pf) Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | supplemental_smartcard | Smartcard Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_apple_watch_unlock_disable | Prevent Apple Watch from Terminating a Session Lock |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_automatic_logout_enforce | Enforce Auto Logout After $ODV Seconds of Inactivity |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_disable | Disable Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_token_removal_enforce | Configure User Session Lock When a Smart Token is Removed |
| ADDED | system_settings_touch_id_settings_disable | Disable the Touch ID System Settings Pane |
| ADDED | system_settings_touchid_unlock_disable | Disable TouchID for Unlocking the Device |
| ADDED | system_settings_usb_restricted_mode | USB Devices Must be Authorized Before Allowing |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |
| ADDED | system_settings_wifi_disable | Disable Wi-Fi Interface |
| ADDED | system_settings_wifi_disable_when_connected_to_ethernet | Disable Wi-Fi When Connected to Ethernet |

## Rule Changes — NIST SP 800-53 Rev 5 — Low (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_failure_halt | Configure System to Shut Down Upon Audit Failure |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fd_configure | Configure System to Audit All Deletions of Object Attributes |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | audit_settings_failure_notify | Configure Audit Failure Notification |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_application_sandboxing | Ensure Separate Execution Domain for Processes |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_config_profile_ui_install_disable | Disable Installation of Configuration Profiles through the User Interface |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_external_storage_access_defined | Access to External Storage Must Be Defined |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_identify_non-org_users | Configure the System to Uniquely Identify and Authenticate Non-Organizational Users |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_implement_cryptography | Configure the System to Implement Approved Cryptography to Protect Information |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_nonlocal_maintenance | Configure the System for Non-local Maintenance |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_policy_banner_ssh_configure | Display Policy Banner at Remote Login |
| ADDED | os_policy_banner_ssh_enforce | Enforce SSH to Display Policy Banner |
| ADDED | os_prohibit_remote_activation_collab_devices | Prohibit Remote Activation of Collaborative Computing Devices |
| ADDED | os_protect_dos_attacks | Protect Against Denial of Service Attacks by Ensuring Rate-Limiting Measures on Network Interfaces |
| ADDED | os_reauth_devices_change_authenticators | Require Devices to Reauthenticate when Changing Authenticators |
| ADDED | os_reauth_users_change_authenticators | Require users to reauthenticate when changing authenticators |
| ADDED | os_required_crypto_module | Ensure all Federal Laws, Executive Orders, Directives, Policies, Regulations, Standards, and Guidance for Authentication to a Cryptographic Module are Met |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_allow_javascript_disable | Disable JavaScript in Safari |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_secure_name_resolution | Secure Name Address Resolution Service |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_per_source_penalties_configure | Configure SSHD PerSourcePenalties |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_sudo_timeout_configure | Configure Sudo Timeout Period to $ODV |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unique_identification | Uniquely Identify Users and Processes |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | supplemental_controls | Out of Scope Supplemental |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_firewall_pf | Packet Filter (pf) Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | supplemental_smartcard | Smartcard Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_touch_id_settings_disable | Disable the Touch ID System Settings Pane |
| ADDED | system_settings_usb_restricted_mode | USB Devices Must be Authorized Before Allowing |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |
| ADDED | system_settings_wifi_disable | Disable Wi-Fi Interface |

## Rule Changes — NIST SP 800-171 Rev 3 (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_failure_halt | Configure System to Shut Down Upon Audit Failure |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | audit_settings_failure_notify | Configure Audit Failure Notification |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_burn_support_disable | Disable Burn Support |
| ADDED | os_config_profile_ui_install_disable | Disable Installation of Configuration Profiles through the User Interface |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_erase_content_and_settings_disable | Disable Erase Content and Settings |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_firewall_default_deny_require | Control Connections to Other Systems via a Deny-All and Allow-by-Exception Firewall Policy |
| ADDED | os_firmware_password_require | Enable Firmware Password |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_implement_cryptography | Configure the System to Implement Approved Cryptography to Protect Information |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_loginwindow_adminhostinfo_disabled | Prevent AdminHostInfo from Being Available at Login Window |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_nonlocal_maintenance | Configure the System for Non-local Maintenance |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_policy_banner_ssh_configure | Display Policy Banner at Remote Login |
| ADDED | os_policy_banner_ssh_enforce | Enforce SSH to Display Policy Banner |
| ADDED | os_prevent_priv_functions | Configure the System to Block Non-Privileged Users from Executing Privileged Functions |
| ADDED | os_prevent_unauthorized_disclosure | Configure the System to Prevent the Unauthorized Disclosure of Data via Shared Resources |
| ADDED | os_privacy_setup_prompt_disable | Disable Privacy Setup Services During Setup Assistant |
| ADDED | os_prohibit_remote_activation_collab_devices | Prohibit Remote Activation of Collaborative Computing Devices |
| ADDED | os_reauth_devices_change_authenticators | Require Devices to Reauthenticate when Changing Authenticators |
| ADDED | os_reauth_privilege | Require users to reauthenticate for privilege escalation |
| ADDED | os_reauth_users_change_authenticators | Require users to reauthenticate when changing authenticators |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_screensaver_loginwindow_enforce | Enforce Screen Saver at Login Window |
| ADDED | os_separate_functionality | Configure the System to Separate User and System Functionality |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_screen_time_prompt_enable | Disable Screen Time Prompt During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_ssh_server_alive_count_max_configure | Set SSH Active Server Alive Maximum to $ODV |
| ADDED | os_ssh_server_alive_interval_configure | Configure SSH ServerAliveInterval option set to $ODV |
| ADDED | os_sshd_channel_timeout_configure | Configure SSHD Channel Timeout to $ODV |
| ADDED | os_sshd_client_alive_count_max_configure | Configure SSHD ClientAliveCountMax to $ODV |
| ADDED | os_sshd_client_alive_interval_configure | Configure SSHD ClientAliveInterval to $ODV |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_unused_connection_timeout_configure | Configure SSHD Unused Connection Timeout to $ODV |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unique_identification | Uniquely Identify Users and Processes |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_50_percent | Require a Minimum of Fifty Percent Character Change in New Passwords |
| ADDED | pwpolicy_account_inactivity_enforce | Disable Accounts after $ODV Days of Inactivity |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | supplemental_controls | Out of Scope Supplemental |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_firewall_pf | Packet Filter (pf) Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | supplemental_smartcard | Smartcard Supplemental |
| ADDED | system_settings_apple_watch_unlock_disable | Prevent Apple Watch from Terminating a Session Lock |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_automatic_logout_enforce | Enforce Auto Logout After $ODV Seconds of Inactivity |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_disable | Disable Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_token_removal_enforce | Configure User Session Lock When a Smart Token is Removed |
| ADDED | system_settings_touchid_unlock_disable | Disable TouchID for Unlocking the Device |
| ADDED | system_settings_wifi_disable_when_connected_to_ethernet | Disable Wi-Fi When Connected to Ethernet |

## Rule Changes — DISA macOS STIG (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_configure_capacity_notify | Configure Audit Capacity Warning |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fd_configure | Configure System to Audit All Deletions of Object Attributes |
| ADDED | audit_flags_fm_configure | Configure System to Audit All Changes of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | audit_settings_failure_notify | Configure Audit Failure Notification |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_certificate_trust_enforce_moderate | Set Smartcard Certificate Trust to Moderate |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_asl_log_files_owner_group_configure | Configure Apple System Log Files Owned by Root and Group to Wheel |
| ADDED | os_asl_log_files_permissions_configure | Configure Apple System Log Files To Mode 640 or Less Permissive |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_camera_disable | Disable Camera |
| ADDED | os_certificate_authority_trust | Issue or Obtain Public Key Certificates from an Approved Service Provider |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_erase_content_and_settings_disable | Disable Erase Content and Settings |
| ADDED | os_facetime_app_disable | Disable FaceTime.app |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_install_log_retention_configure | Configure Install.log Retention to $ODV |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_loginwindow_adminhostinfo_disabled | Prevent AdminHostInfo from Being Available at Login Window |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_newsyslog_files_owner_group_configure | Configure System Log Files Owned by Root and Group to Wheel |
| ADDED | os_newsyslog_files_permissions_configure | Configure System Log Files to Mode 640 or Less Permissive |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_hint_remove | Remove Password Hint From User Accounts |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_policy_banner_ssh_configure | Display Policy Banner at Remote Login |
| ADDED | os_policy_banner_ssh_enforce | Enforce SSH to Display Policy Banner |
| ADDED | os_privacy_setup_prompt_disable | Disable Privacy Setup Services During Setup Assistant |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_secure_boot_verify | Ensure Secure Boot Level Set to Full |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_screen_time_prompt_enable | Disable Screen Time Prompt During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_ssh_server_alive_count_max_configure | Set SSH Active Server Alive Maximum to $ODV |
| ADDED | os_ssh_server_alive_interval_configure | Configure SSH ServerAliveInterval option set to $ODV |
| ADDED | os_sshd_channel_timeout_configure | Configure SSHD Channel Timeout to $ODV |
| ADDED | os_sshd_client_alive_count_max_configure | Configure SSHD ClientAliveCountMax to $ODV |
| ADDED | os_sshd_client_alive_interval_configure | Configure SSHD ClientAliveInterval to $ODV |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_login_grace_time_configure | Set Login Grace Time to $ODV |
| ADDED | os_sshd_permit_root_login_configure | Disable Root Login for SSH |
| ADDED | os_sshd_unused_connection_timeout_configure | Configure SSHD Unused Connection Timeout to $ODV |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudo_timeout_configure | Configure Sudo Timeout Period to $ODV |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_supported_operating_system | The macOS Version Must Be Supported by the Vendor |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_user_app_installation_prohibit | Prohibit User Installation of Software into /Users/ |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_inactivity_enforce | Disable Accounts after $ODV Days of Inactivity |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_alpha_numeric_enforce | Require Passwords Contain a Minimum of One Numeric Character |
| ADDED | pwpolicy_custom_regex_enforce | Require Passwords to Match the Defined Custom Regular Expression |
| ADDED | pwpolicy_max_lifetime_enforce | Restrict Maximum Password Lifetime to $ODV Days |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_minimum_lifetime_enforce | Set Minimum Password Lifetime to $ODV Hours |
| ADDED | pwpolicy_special_character_enforce | Require Passwords Contain a Minimum of One Special Character |
| ADDED | pwpolicy_temporary_or_emergency_accounts_disable | Automatically Remove or Disable Temporary or Emergency User Accounts within 72 Hours |
| ADDED | supplemental_controls | Out of Scope Supplemental |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_firewall_pf | Packet Filter (pf) Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | supplemental_smartcard | Smartcard Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_apple_watch_unlock_disable | Prevent Apple Watch from Terminating a Session Lock |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_automatic_logout_enforce | Enforce Auto Logout After $ODV Seconds of Inactivity |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_disable | Disable Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_token_removal_enforce | Configure User Session Lock When a Smart Token is Removed |
| ADDED | system_settings_touchid_unlock_disable | Disable TouchID for Unlocking the Device |
| ADDED | system_settings_usb_restricted_mode | USB Devices Must be Authorized Before Allowing |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |

## Rule Changes — CMMC 2.0 — Level 1 (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_auth_peripherals | Must Authenticate Before Establishing a Connection |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_firmware_password_require | Enable Firmware Password |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | supplemental_controls | Out of Scope Supplemental |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_firewall_pf | Packet Filter (pf) Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | supplemental_smartcard | Smartcard Supplemental |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |

## Rule Changes — CMMC 2.0 — Level 2 (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_failure_halt | Configure System to Shut Down Upon Audit Failure |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fd_configure | Configure System to Audit All Deletions of Object Attributes |
| ADDED | audit_flags_fm_configure | Configure System to Audit All Changes of Object Attributes |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_record_reduction_report_generation | Audit Record Reduction and Report Generation |
| ADDED | audit_records_processing | Audit Record Reduction and Report Generation |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | audit_settings_failure_notify | Configure Audit Failure Notification |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_certificate_trust_enforce_high | Set Smartcard Certificate Trust to High |
| ADDED | auth_smartcard_certificate_trust_enforce_moderate | Set Smartcard Certificate Trust to Moderate |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_auth_peripherals | Must Authenticate Before Establishing a Connection |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_blank_bluray_disable | Disable Blank Blu Ray |
| ADDED | os_blank_cd_disable | Disable Blank CD |
| ADDED | os_blank_dvd_disable | Disable Blank DVD |
| ADDED | os_bluray_read_only_enforce | Enforce Blu Ray Read Only |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_burn_support_disable | Disable Burn Support |
| ADDED | os_cd_read_only_enforce | Enforce CD Read Only |
| ADDED | os_certificate_authority_trust | Issue or Obtain Public Key Certificates from an Approved Service Provider |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_config_profile_ui_install_disable | Disable Installation of Configuration Profiles through the User Interface |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_disk_image_disable | Disable Disk Images |
| ADDED | os_dvdram_disable | Disable DVD-RAM |
| ADDED | os_erase_content_and_settings_disable | Disable Erase Content and Settings |
| ADDED | os_external_storage_access_defined | Access to External Storage Must Be Defined |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_firewall_default_deny_require | Control Connections to Other Systems via a Deny-All and Allow-by-Exception Firewall Policy |
| ADDED | os_firmware_password_require | Enable Firmware Password |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_implement_cryptography | Configure the System to Implement Approved Cryptography to Protect Information |
| ADDED | os_install_log_retention_configure | Configure Install.log Retention to $ODV |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_managed_access_control_points | Managed Access Control Points |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_nonlocal_maintenance | Configure the System for Non-local Maintenance |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_hint_remove | Remove Password Hint From User Accounts |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_policy_banner_ssh_configure | Display Policy Banner at Remote Login |
| ADDED | os_policy_banner_ssh_enforce | Enforce SSH to Display Policy Banner |
| ADDED | os_power_nap_disable | Disable Power Nap |
| ADDED | os_prevent_priv_functions | Configure the System to Block Non-Privileged Users from Executing Privileged Functions |
| ADDED | os_prevent_unauthorized_disclosure | Configure the System to Prevent the Unauthorized Disclosure of Data via Shared Resources |
| ADDED | os_privacy_setup_prompt_disable | Disable Privacy Setup Services During Setup Assistant |
| ADDED | os_prohibit_remote_activation_collab_devices | Prohibit Remote Activation of Collaborative Computing Devices |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_removable_media_disable | Disable Removable Storage Devices |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_screensaver_loginwindow_enforce | Enforce Screen Saver at Login Window |
| ADDED | os_secure_enclave | Protected Storage for Cryptographic Keys |
| ADDED | os_separate_functionality | Configure the System to Separate User and System Functionality |
| ADDED | os_setup_assistant_filevault_enforce | Enforce FileVault in Setup Assistant |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_screen_time_prompt_enable | Disable Screen Time Prompt During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_ssh_server_alive_count_max_configure | Set SSH Active Server Alive Maximum to $ODV |
| ADDED | os_ssh_server_alive_interval_configure | Configure SSH ServerAliveInterval option set to $ODV |
| ADDED | os_sshd_channel_timeout_configure | Configure SSHD Channel Timeout to $ODV |
| ADDED | os_sshd_client_alive_count_max_configure | Configure SSHD ClientAliveCountMax to $ODV |
| ADDED | os_sshd_client_alive_interval_configure | Configure SSHD ClientAliveInterval to $ODV |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_login_grace_time_configure | Set Login Grace Time to $ODV |
| ADDED | os_sshd_unused_connection_timeout_configure | Configure SSHD Unused Connection Timeout to $ODV |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unique_identification | Uniquely Identify Users and Processes |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_user_app_installation_prohibit | Prohibit User Installation of Software into /Users/ |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_inactivity_enforce | Disable Accounts after $ODV Days of Inactivity |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_alpha_numeric_enforce | Require Passwords Contain a Minimum of One Numeric Character |
| ADDED | pwpolicy_custom_regex_enforce | Require Passwords to Match the Defined Custom Regular Expression |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_max_lifetime_enforce | Restrict Maximum Password Lifetime to $ODV Days |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_minimum_lifetime_enforce | Set Minimum Password Lifetime to $ODV Hours |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | pwpolicy_special_character_enforce | Require Passwords Contain a Minimum of One Special Character |
| ADDED | supplemental_controls | Out of Scope Supplemental |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_firewall_pf | Packet Filter (pf) Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | supplemental_smartcard | Smartcard Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_apple_watch_unlock_disable | Prevent Apple Watch from Terminating a Session Lock |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_automatic_logout_enforce | Enforce Auto Logout After $ODV Seconds of Inactivity |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_disable | Disable Hot Corners |
| ADDED | system_settings_hot_corners_secure | Secure Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_token_removal_enforce | Configure User Session Lock When a Smart Token is Removed |
| ADDED | system_settings_touch_id_settings_disable | Disable the Touch ID System Settings Pane |
| ADDED | system_settings_touchid_unlock_disable | Disable TouchID for Unlocking the Device |
| ADDED | system_settings_usb_restricted_mode | USB Devices Must be Authorized Before Allowing |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |
| ADDED | system_settings_wifi_disable | Disable Wi-Fi Interface |
| ADDED | system_settings_wifi_disable_when_connected_to_ethernet | Disable Wi-Fi When Connected to Ethernet |

## Rule Changes — CNSSI 1253 — High (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_configure_capacity_notify | Configure Audit Capacity Warning |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_enforce_dual_auth | Enforce Dual Authorization for Movement and Deletion of Audit Information |
| ADDED | audit_failure_halt | Configure System to Shut Down Upon Audit Failure |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fd_configure | Configure System to Audit All Deletions of Object Attributes |
| ADDED | audit_flags_fm_configure | Configure System to Audit All Changes of Object Attributes |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_off_load_records | Off-Load Audit Records |
| ADDED | audit_record_reduction_report_generation | Audit Record Reduction and Report Generation |
| ADDED | audit_records_processing | Audit Record Reduction and Report Generation |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | audit_settings_failure_notify | Configure Audit Failure Notification |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_certificate_trust_enforce_high | Set Smartcard Certificate Trust to High |
| ADDED | auth_smartcard_certificate_trust_enforce_moderate | Set Smartcard Certificate Trust to Moderate |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_allow_info_passed | Allow Information Transfer with Other Operating Systems |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_application_sandboxing | Ensure Separate Execution Domain for Processes |
| ADDED | os_asl_log_files_owner_group_configure | Configure Apple System Log Files Owned by Root and Group to Wheel |
| ADDED | os_asl_log_files_permissions_configure | Configure Apple System Log Files To Mode 640 or Less Permissive |
| ADDED | os_auth_peripherals | Must Authenticate Before Establishing a Connection |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_blank_bluray_disable | Disable Blank Blu Ray |
| ADDED | os_blank_cd_disable | Disable Blank CD |
| ADDED | os_blank_dvd_disable | Disable Blank DVD |
| ADDED | os_bluray_read_only_enforce | Enforce Blu Ray Read Only |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_burn_support_disable | Disable Burn Support |
| ADDED | os_calendar_app_disable | Disable Calendar.app |
| ADDED | os_cd_read_only_enforce | Enforce CD Read Only |
| ADDED | os_certificate_authority_trust | Issue or Obtain Public Key Certificates from an Approved Service Provider |
| ADDED | os_change_security_attributes | Allow Administrators to Modify Security Settings and System Attributes |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_config_profile_ui_install_disable | Disable Installation of Configuration Profiles through the User Interface |
| ADDED | os_continuous_monitoring | Configure Automated Flaw Remediation |
| ADDED | os_crypto_audit | Protect Audit Integrity with Cryptographic Mechanisms |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_disk_image_disable | Disable Disk Images |
| ADDED | os_dvdram_disable | Disable DVD-RAM |
| ADDED | os_enforce_access_restrictions | Enforce Access Restrictions |
| ADDED | os_erase_content_and_settings_disable | Disable Erase Content and Settings |
| ADDED | os_external_storage_access_defined | Access to External Storage Must Be Defined |
| ADDED | os_facetime_app_disable | Disable FaceTime.app |
| ADDED | os_fail_secure_state | Configure System to Fail to a Known Safe State if System Initialization, Shutdown, or Abort Fails |
| ADDED | os_filevault_authorized_users | FileVault Authorized Users |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_firewall_default_deny_require | Control Connections to Other Systems via a Deny-All and Allow-by-Exception Firewall Policy |
| ADDED | os_firmware_password_require | Enable Firmware Password |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_grant_privs | Allow Administrators to Promote Other Users to Administrator Status |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_default | Configure User's Home Folders to Apple's Default |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_identify_non-org_users | Configure the System to Uniquely Identify and Authenticate Non-Organizational Users |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_implement_cryptography | Configure the System to Implement Approved Cryptography to Protect Information |
| ADDED | os_implement_memory_protection | Configure the System to Protect Memory from Unauthorized Code Execution |
| ADDED | os_information_validation | Information Input Validation |
| ADDED | os_install_log_retention_configure | Configure Install.log Retention to $ODV |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_isolate_security_functions | Configure the System to Separate User and System Functionality |
| ADDED | os_limit_dos_attacks | Limit Impact of Denial of Service Attacks |
| ADDED | os_limit_gui_sessions | Limit Concurrent GUI Sessions to 10 for all Accounts |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_loginwindow_adminhostinfo_disabled | Prevent AdminHostInfo from Being Available at Login Window |
| ADDED | os_logoff_capability_and_message | Display logoff capability and message to prevent exploitation |
| ADDED | os_mail_app_disable | Disable Mail App |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_managed_access_control_points | Managed Access Control Points |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_messages_app_disable | Disable Messages App |
| ADDED | os_newsyslog_files_owner_group_configure | Configure System Log Files Owned by Root and Group to Wheel |
| ADDED | os_newsyslog_files_permissions_configure | Configure System Log Files to Mode 640 or Less Permissive |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_non_repudiation | Non-Repudiation |
| ADDED | os_nonlocal_maintenance | Configure the System for Non-local Maintenance |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_notify_unauthorized_baseline_change | Configure the System to Notify upon Baseline Configuration Changes |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_parental_controls_enable | Enable Parental Controls |
| ADDED | os_password_autofill_disable | Disable Password Autofill |
| ADDED | os_password_hint_remove | Remove Password Hint From User Accounts |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_policy_banner_ssh_configure | Display Policy Banner at Remote Login |
| ADDED | os_policy_banner_ssh_enforce | Enforce SSH to Display Policy Banner |
| ADDED | os_power_nap_disable | Disable Power Nap |
| ADDED | os_predictable_behavior | Must behave in predictable and documented manner |
| ADDED | os_prevent_priv_execution | Prevent Software From Executing at Higher Privilege Levels than Users Executing The Software |
| ADDED | os_prevent_priv_functions | Configure the System to Block Non-Privileged Users from Executing Privileged Functions |
| ADDED | os_prevent_unauthorized_disclosure | Configure the System to Prevent the Unauthorized Disclosure of Data via Shared Resources |
| ADDED | os_privacy_setup_prompt_disable | Disable Privacy Setup Services During Setup Assistant |
| ADDED | os_prohibit_remote_activation_collab_devices | Prohibit Remote Activation of Collaborative Computing Devices |
| ADDED | os_protect_dos_attacks | Protect Against Denial of Service Attacks by Ensuring Rate-Limiting Measures on Network Interfaces |
| ADDED | os_provide_automated_account_management | Employ Automated Mechanisms for Account Management Functions |
| ADDED | os_provide_disconnect_remote_access | Provide Ability to Disconnect or Disable Remote Access |
| ADDED | os_reauth_devices_change_authenticators | Require Devices to Reauthenticate when Changing Authenticators |
| ADDED | os_reauth_privilege | Require users to reauthenticate for privilege escalation |
| ADDED | os_reauth_users_change_authenticators | Require users to reauthenticate when changing authenticators |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_removable_media_disable | Disable Removable Storage Devices |
| ADDED | os_remove_software_components_after_updates | Must remove all software components after updated versions installed |
| ADDED | os_required_crypto_module | Ensure all Federal Laws, Executive Orders, Directives, Policies, Regulations, Standards, and Guidance for Authentication to a Cryptographic Module are Met |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_screensaver_loginwindow_enforce | Enforce Screen Saver at Login Window |
| ADDED | os_secure_boot_verify | Ensure Secure Boot Level Set to Full |
| ADDED | os_secure_enclave | Protected Storage for Cryptographic Keys |
| ADDED | os_secure_name_resolution | Secure Name Address Resolution Service |
| ADDED | os_separate_functionality | Configure the System to Separate User and System Functionality |
| ADDED | os_setup_assistant_filevault_enforce | Enforce FileVault in Setup Assistant |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_screen_time_prompt_enable | Disable Screen Time Prompt During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_ssh_server_alive_count_max_configure | Set SSH Active Server Alive Maximum to $ODV |
| ADDED | os_ssh_server_alive_interval_configure | Configure SSH ServerAliveInterval option set to $ODV |
| ADDED | os_sshd_channel_timeout_configure | Configure SSHD Channel Timeout to $ODV |
| ADDED | os_sshd_client_alive_count_max_configure | Configure SSHD ClientAliveCountMax to $ODV |
| ADDED | os_sshd_client_alive_interval_configure | Configure SSHD ClientAliveInterval to $ODV |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_login_grace_time_configure | Set Login Grace Time to $ODV |
| ADDED | os_sshd_per_source_penalties_configure | Configure SSHD PerSourcePenalties |
| ADDED | os_sshd_permit_root_login_configure | Disable Root Login for SSH |
| ADDED | os_sshd_unused_connection_timeout_configure | Configure SSHD Unused Connection Timeout to $ODV |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_system_read_only | Ensure System Volume is Read Only |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unique_identification | Uniquely Identify Users and Processes |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_user_app_installation_prohibit | Prohibit User Installation of Software into /Users/ |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_verify_remote_disconnection | Verify remote disconnection of sessions |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_inactivity_enforce | Disable Accounts after $ODV Days of Inactivity |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_alpha_numeric_enforce | Require Passwords Contain a Minimum of One Numeric Character |
| ADDED | pwpolicy_custom_regex_enforce | Require Passwords to Match the Defined Custom Regular Expression |
| ADDED | pwpolicy_emergency_accounts_disable | Automatically Remove or Disable Emergency Accounts within 72 Hours |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_lower_case_character_enforce | Require Passwords Contain a Minimum of One Lowercase Character |
| ADDED | pwpolicy_max_lifetime_enforce | Restrict Maximum Password Lifetime to $ODV Days |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_minimum_lifetime_enforce | Set Minimum Password Lifetime to $ODV Hours |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | pwpolicy_special_character_enforce | Require Passwords Contain a Minimum of One Special Character |
| ADDED | pwpolicy_temporary_accounts_disable | Automatically Remove or Disable Temporary User Accounts within 72 Hours |
| ADDED | pwpolicy_temporary_or_emergency_accounts_disable | Automatically Remove or Disable Temporary or Emergency User Accounts within 72 Hours |
| ADDED | pwpolicy_upper_case_character_enforce | Require Passwords Contain a Minimum of One Uppercase Character |
| ADDED | supplemental_controls | Out of Scope Supplemental |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_firewall_pf | Packet Filter (pf) Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | supplemental_smartcard | Smartcard Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_apple_watch_unlock_disable | Prevent Apple Watch from Terminating a Session Lock |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_automatic_logout_enforce | Enforce Auto Logout After $ODV Seconds of Inactivity |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_disable | Disable Hot Corners |
| ADDED | system_settings_hot_corners_secure | Secure Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_token_removal_enforce | Configure User Session Lock When a Smart Token is Removed |
| ADDED | system_settings_touch_id_settings_disable | Disable the Touch ID System Settings Pane |
| ADDED | system_settings_touchid_unlock_disable | Disable TouchID for Unlocking the Device |
| ADDED | system_settings_usb_restricted_mode | USB Devices Must be Authorized Before Allowing |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |
| ADDED | system_settings_wifi_disable | Disable Wi-Fi Interface |
| ADDED | system_settings_wifi_disable_when_connected_to_ethernet | Disable Wi-Fi When Connected to Ethernet |

## Rule Changes — CNSSI 1253 — Moderate (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_configure_capacity_notify | Configure Audit Capacity Warning |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_failure_halt | Configure System to Shut Down Upon Audit Failure |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fd_configure | Configure System to Audit All Deletions of Object Attributes |
| ADDED | audit_flags_fm_configure | Configure System to Audit All Changes of Object Attributes |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_off_load_records | Off-Load Audit Records |
| ADDED | audit_record_reduction_report_generation | Audit Record Reduction and Report Generation |
| ADDED | audit_records_processing | Audit Record Reduction and Report Generation |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | audit_settings_failure_notify | Configure Audit Failure Notification |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_certificate_trust_enforce_high | Set Smartcard Certificate Trust to High |
| ADDED | auth_smartcard_certificate_trust_enforce_moderate | Set Smartcard Certificate Trust to Moderate |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_allow_info_passed | Allow Information Transfer with Other Operating Systems |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_application_sandboxing | Ensure Separate Execution Domain for Processes |
| ADDED | os_asl_log_files_owner_group_configure | Configure Apple System Log Files Owned by Root and Group to Wheel |
| ADDED | os_asl_log_files_permissions_configure | Configure Apple System Log Files To Mode 640 or Less Permissive |
| ADDED | os_auth_peripherals | Must Authenticate Before Establishing a Connection |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_blank_bluray_disable | Disable Blank Blu Ray |
| ADDED | os_blank_cd_disable | Disable Blank CD |
| ADDED | os_blank_dvd_disable | Disable Blank DVD |
| ADDED | os_bluray_read_only_enforce | Enforce Blu Ray Read Only |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_burn_support_disable | Disable Burn Support |
| ADDED | os_calendar_app_disable | Disable Calendar.app |
| ADDED | os_cd_read_only_enforce | Enforce CD Read Only |
| ADDED | os_certificate_authority_trust | Issue or Obtain Public Key Certificates from an Approved Service Provider |
| ADDED | os_change_security_attributes | Allow Administrators to Modify Security Settings and System Attributes |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_config_profile_ui_install_disable | Disable Installation of Configuration Profiles through the User Interface |
| ADDED | os_continuous_monitoring | Configure Automated Flaw Remediation |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_disk_image_disable | Disable Disk Images |
| ADDED | os_dvdram_disable | Disable DVD-RAM |
| ADDED | os_enforce_access_restrictions | Enforce Access Restrictions |
| ADDED | os_erase_content_and_settings_disable | Disable Erase Content and Settings |
| ADDED | os_external_storage_access_defined | Access to External Storage Must Be Defined |
| ADDED | os_facetime_app_disable | Disable FaceTime.app |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_firewall_default_deny_require | Control Connections to Other Systems via a Deny-All and Allow-by-Exception Firewall Policy |
| ADDED | os_firmware_password_require | Enable Firmware Password |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_grant_privs | Allow Administrators to Promote Other Users to Administrator Status |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_default | Configure User's Home Folders to Apple's Default |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_identify_non-org_users | Configure the System to Uniquely Identify and Authenticate Non-Organizational Users |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_implement_cryptography | Configure the System to Implement Approved Cryptography to Protect Information |
| ADDED | os_implement_memory_protection | Configure the System to Protect Memory from Unauthorized Code Execution |
| ADDED | os_information_validation | Information Input Validation |
| ADDED | os_install_log_retention_configure | Configure Install.log Retention to $ODV |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_limit_dos_attacks | Limit Impact of Denial of Service Attacks |
| ADDED | os_limit_gui_sessions | Limit Concurrent GUI Sessions to 10 for all Accounts |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_loginwindow_adminhostinfo_disabled | Prevent AdminHostInfo from Being Available at Login Window |
| ADDED | os_logoff_capability_and_message | Display logoff capability and message to prevent exploitation |
| ADDED | os_mail_app_disable | Disable Mail App |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_managed_access_control_points | Managed Access Control Points |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_messages_app_disable | Disable Messages App |
| ADDED | os_newsyslog_files_owner_group_configure | Configure System Log Files Owned by Root and Group to Wheel |
| ADDED | os_newsyslog_files_permissions_configure | Configure System Log Files to Mode 640 or Less Permissive |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_non_repudiation | Non-Repudiation |
| ADDED | os_nonlocal_maintenance | Configure the System for Non-local Maintenance |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_parental_controls_enable | Enable Parental Controls |
| ADDED | os_password_autofill_disable | Disable Password Autofill |
| ADDED | os_password_hint_remove | Remove Password Hint From User Accounts |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_policy_banner_ssh_configure | Display Policy Banner at Remote Login |
| ADDED | os_policy_banner_ssh_enforce | Enforce SSH to Display Policy Banner |
| ADDED | os_power_nap_disable | Disable Power Nap |
| ADDED | os_predictable_behavior | Must behave in predictable and documented manner |
| ADDED | os_prevent_priv_execution | Prevent Software From Executing at Higher Privilege Levels than Users Executing The Software |
| ADDED | os_prevent_priv_functions | Configure the System to Block Non-Privileged Users from Executing Privileged Functions |
| ADDED | os_prevent_unauthorized_disclosure | Configure the System to Prevent the Unauthorized Disclosure of Data via Shared Resources |
| ADDED | os_privacy_setup_prompt_disable | Disable Privacy Setup Services During Setup Assistant |
| ADDED | os_prohibit_remote_activation_collab_devices | Prohibit Remote Activation of Collaborative Computing Devices |
| ADDED | os_protect_dos_attacks | Protect Against Denial of Service Attacks by Ensuring Rate-Limiting Measures on Network Interfaces |
| ADDED | os_provide_automated_account_management | Employ Automated Mechanisms for Account Management Functions |
| ADDED | os_provide_disconnect_remote_access | Provide Ability to Disconnect or Disable Remote Access |
| ADDED | os_reauth_devices_change_authenticators | Require Devices to Reauthenticate when Changing Authenticators |
| ADDED | os_reauth_privilege | Require users to reauthenticate for privilege escalation |
| ADDED | os_reauth_users_change_authenticators | Require users to reauthenticate when changing authenticators |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_removable_media_disable | Disable Removable Storage Devices |
| ADDED | os_remove_software_components_after_updates | Must remove all software components after updated versions installed |
| ADDED | os_required_crypto_module | Ensure all Federal Laws, Executive Orders, Directives, Policies, Regulations, Standards, and Guidance for Authentication to a Cryptographic Module are Met |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_screensaver_loginwindow_enforce | Enforce Screen Saver at Login Window |
| ADDED | os_secure_boot_verify | Ensure Secure Boot Level Set to Full |
| ADDED | os_secure_enclave | Protected Storage for Cryptographic Keys |
| ADDED | os_secure_name_resolution | Secure Name Address Resolution Service |
| ADDED | os_separate_functionality | Configure the System to Separate User and System Functionality |
| ADDED | os_setup_assistant_filevault_enforce | Enforce FileVault in Setup Assistant |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_screen_time_prompt_enable | Disable Screen Time Prompt During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_ssh_server_alive_count_max_configure | Set SSH Active Server Alive Maximum to $ODV |
| ADDED | os_ssh_server_alive_interval_configure | Configure SSH ServerAliveInterval option set to $ODV |
| ADDED | os_sshd_channel_timeout_configure | Configure SSHD Channel Timeout to $ODV |
| ADDED | os_sshd_client_alive_count_max_configure | Configure SSHD ClientAliveCountMax to $ODV |
| ADDED | os_sshd_client_alive_interval_configure | Configure SSHD ClientAliveInterval to $ODV |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_login_grace_time_configure | Set Login Grace Time to $ODV |
| ADDED | os_sshd_per_source_penalties_configure | Configure SSHD PerSourcePenalties |
| ADDED | os_sshd_permit_root_login_configure | Disable Root Login for SSH |
| ADDED | os_sshd_unused_connection_timeout_configure | Configure SSHD Unused Connection Timeout to $ODV |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_system_read_only | Ensure System Volume is Read Only |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unique_identification | Uniquely Identify Users and Processes |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_user_app_installation_prohibit | Prohibit User Installation of Software into /Users/ |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_verify_remote_disconnection | Verify remote disconnection of sessions |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_inactivity_enforce | Disable Accounts after $ODV Days of Inactivity |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_alpha_numeric_enforce | Require Passwords Contain a Minimum of One Numeric Character |
| ADDED | pwpolicy_custom_regex_enforce | Require Passwords to Match the Defined Custom Regular Expression |
| ADDED | pwpolicy_emergency_accounts_disable | Automatically Remove or Disable Emergency Accounts within 72 Hours |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_lower_case_character_enforce | Require Passwords Contain a Minimum of One Lowercase Character |
| ADDED | pwpolicy_max_lifetime_enforce | Restrict Maximum Password Lifetime to $ODV Days |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_minimum_lifetime_enforce | Set Minimum Password Lifetime to $ODV Hours |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | pwpolicy_special_character_enforce | Require Passwords Contain a Minimum of One Special Character |
| ADDED | pwpolicy_temporary_accounts_disable | Automatically Remove or Disable Temporary User Accounts within 72 Hours |
| ADDED | pwpolicy_temporary_or_emergency_accounts_disable | Automatically Remove or Disable Temporary or Emergency User Accounts within 72 Hours |
| ADDED | pwpolicy_upper_case_character_enforce | Require Passwords Contain a Minimum of One Uppercase Character |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_apple_watch_unlock_disable | Prevent Apple Watch from Terminating a Session Lock |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_automatic_logout_enforce | Enforce Auto Logout After $ODV Seconds of Inactivity |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_disable | Disable Hot Corners |
| ADDED | system_settings_hot_corners_secure | Secure Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_token_removal_enforce | Configure User Session Lock When a Smart Token is Removed |
| ADDED | system_settings_touch_id_settings_disable | Disable the Touch ID System Settings Pane |
| ADDED | system_settings_touchid_unlock_disable | Disable TouchID for Unlocking the Device |
| ADDED | system_settings_usb_restricted_mode | USB Devices Must be Authorized Before Allowing |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |
| ADDED | system_settings_wifi_disable | Disable Wi-Fi Interface |
| ADDED | system_settings_wifi_disable_when_connected_to_ethernet | Disable Wi-Fi When Connected to Ethernet |

## Rule Changes — CNSSI 1253 — Low (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_configure_capacity_notify | Configure Audit Capacity Warning |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_failure_halt | Configure System to Shut Down Upon Audit Failure |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fd_configure | Configure System to Audit All Deletions of Object Attributes |
| ADDED | audit_flags_fm_configure | Configure System to Audit All Changes of Object Attributes |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_off_load_records | Off-Load Audit Records |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | audit_settings_failure_notify | Configure Audit Failure Notification |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_certificate_trust_enforce_high | Set Smartcard Certificate Trust to High |
| ADDED | auth_smartcard_certificate_trust_enforce_moderate | Set Smartcard Certificate Trust to Moderate |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_allow_info_passed | Allow Information Transfer with Other Operating Systems |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_application_sandboxing | Ensure Separate Execution Domain for Processes |
| ADDED | os_asl_log_files_owner_group_configure | Configure Apple System Log Files Owned by Root and Group to Wheel |
| ADDED | os_asl_log_files_permissions_configure | Configure Apple System Log Files To Mode 640 or Less Permissive |
| ADDED | os_auth_peripherals | Must Authenticate Before Establishing a Connection |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_blank_bluray_disable | Disable Blank Blu Ray |
| ADDED | os_blank_cd_disable | Disable Blank CD |
| ADDED | os_blank_dvd_disable | Disable Blank DVD |
| ADDED | os_bluray_read_only_enforce | Enforce Blu Ray Read Only |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_burn_support_disable | Disable Burn Support |
| ADDED | os_calendar_app_disable | Disable Calendar.app |
| ADDED | os_cd_read_only_enforce | Enforce CD Read Only |
| ADDED | os_certificate_authority_trust | Issue or Obtain Public Key Certificates from an Approved Service Provider |
| ADDED | os_change_security_attributes | Allow Administrators to Modify Security Settings and System Attributes |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_config_profile_ui_install_disable | Disable Installation of Configuration Profiles through the User Interface |
| ADDED | os_continuous_monitoring | Configure Automated Flaw Remediation |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_disk_image_disable | Disable Disk Images |
| ADDED | os_dvdram_disable | Disable DVD-RAM |
| ADDED | os_erase_content_and_settings_disable | Disable Erase Content and Settings |
| ADDED | os_external_storage_access_defined | Access to External Storage Must Be Defined |
| ADDED | os_facetime_app_disable | Disable FaceTime.app |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_firewall_default_deny_require | Control Connections to Other Systems via a Deny-All and Allow-by-Exception Firewall Policy |
| ADDED | os_firmware_password_require | Enable Firmware Password |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_grant_privs | Allow Administrators to Promote Other Users to Administrator Status |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_default | Configure User's Home Folders to Apple's Default |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_identify_non-org_users | Configure the System to Uniquely Identify and Authenticate Non-Organizational Users |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_implement_cryptography | Configure the System to Implement Approved Cryptography to Protect Information |
| ADDED | os_information_validation | Information Input Validation |
| ADDED | os_install_log_retention_configure | Configure Install.log Retention to $ODV |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_loginwindow_adminhostinfo_disabled | Prevent AdminHostInfo from Being Available at Login Window |
| ADDED | os_logoff_capability_and_message | Display logoff capability and message to prevent exploitation |
| ADDED | os_mail_app_disable | Disable Mail App |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_managed_access_control_points | Managed Access Control Points |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_messages_app_disable | Disable Messages App |
| ADDED | os_newsyslog_files_owner_group_configure | Configure System Log Files Owned by Root and Group to Wheel |
| ADDED | os_newsyslog_files_permissions_configure | Configure System Log Files to Mode 640 or Less Permissive |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_nonlocal_maintenance | Configure the System for Non-local Maintenance |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_parental_controls_enable | Enable Parental Controls |
| ADDED | os_password_autofill_disable | Disable Password Autofill |
| ADDED | os_password_hint_remove | Remove Password Hint From User Accounts |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_policy_banner_ssh_configure | Display Policy Banner at Remote Login |
| ADDED | os_policy_banner_ssh_enforce | Enforce SSH to Display Policy Banner |
| ADDED | os_power_nap_disable | Disable Power Nap |
| ADDED | os_predictable_behavior | Must behave in predictable and documented manner |
| ADDED | os_prevent_priv_execution | Prevent Software From Executing at Higher Privilege Levels than Users Executing The Software |
| ADDED | os_prevent_priv_functions | Configure the System to Block Non-Privileged Users from Executing Privileged Functions |
| ADDED | os_prevent_unauthorized_disclosure | Configure the System to Prevent the Unauthorized Disclosure of Data via Shared Resources |
| ADDED | os_privacy_setup_prompt_disable | Disable Privacy Setup Services During Setup Assistant |
| ADDED | os_prohibit_remote_activation_collab_devices | Prohibit Remote Activation of Collaborative Computing Devices |
| ADDED | os_protect_dos_attacks | Protect Against Denial of Service Attacks by Ensuring Rate-Limiting Measures on Network Interfaces |
| ADDED | os_provide_disconnect_remote_access | Provide Ability to Disconnect or Disable Remote Access |
| ADDED | os_reauth_devices_change_authenticators | Require Devices to Reauthenticate when Changing Authenticators |
| ADDED | os_reauth_privilege | Require users to reauthenticate for privilege escalation |
| ADDED | os_reauth_users_change_authenticators | Require users to reauthenticate when changing authenticators |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_removable_media_disable | Disable Removable Storage Devices |
| ADDED | os_remove_software_components_after_updates | Must remove all software components after updated versions installed |
| ADDED | os_required_crypto_module | Ensure all Federal Laws, Executive Orders, Directives, Policies, Regulations, Standards, and Guidance for Authentication to a Cryptographic Module are Met |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_screensaver_loginwindow_enforce | Enforce Screen Saver at Login Window |
| ADDED | os_secure_enclave | Protected Storage for Cryptographic Keys |
| ADDED | os_secure_name_resolution | Secure Name Address Resolution Service |
| ADDED | os_separate_functionality | Configure the System to Separate User and System Functionality |
| ADDED | os_setup_assistant_filevault_enforce | Enforce FileVault in Setup Assistant |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_screen_time_prompt_enable | Disable Screen Time Prompt During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_ssh_server_alive_count_max_configure | Set SSH Active Server Alive Maximum to $ODV |
| ADDED | os_ssh_server_alive_interval_configure | Configure SSH ServerAliveInterval option set to $ODV |
| ADDED | os_sshd_channel_timeout_configure | Configure SSHD Channel Timeout to $ODV |
| ADDED | os_sshd_client_alive_count_max_configure | Configure SSHD ClientAliveCountMax to $ODV |
| ADDED | os_sshd_client_alive_interval_configure | Configure SSHD ClientAliveInterval to $ODV |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_login_grace_time_configure | Set Login Grace Time to $ODV |
| ADDED | os_sshd_per_source_penalties_configure | Configure SSHD PerSourcePenalties |
| ADDED | os_sshd_permit_root_login_configure | Disable Root Login for SSH |
| ADDED | os_sshd_unused_connection_timeout_configure | Configure SSHD Unused Connection Timeout to $ODV |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_system_read_only | Ensure System Volume is Read Only |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unique_identification | Uniquely Identify Users and Processes |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_user_app_installation_prohibit | Prohibit User Installation of Software into /Users/ |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_verify_remote_disconnection | Verify remote disconnection of sessions |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_alpha_numeric_enforce | Require Passwords Contain a Minimum of One Numeric Character |
| ADDED | pwpolicy_custom_regex_enforce | Require Passwords to Match the Defined Custom Regular Expression |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_lower_case_character_enforce | Require Passwords Contain a Minimum of One Lowercase Character |
| ADDED | pwpolicy_max_lifetime_enforce | Restrict Maximum Password Lifetime to $ODV Days |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_minimum_lifetime_enforce | Set Minimum Password Lifetime to $ODV Hours |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | pwpolicy_special_character_enforce | Require Passwords Contain a Minimum of One Special Character |
| ADDED | pwpolicy_upper_case_character_enforce | Require Passwords Contain a Minimum of One Uppercase Character |
| ADDED | supplemental_controls | Out of Scope Supplemental |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_firewall_pf | Packet Filter (pf) Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | supplemental_smartcard | Smartcard Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_apple_watch_unlock_disable | Prevent Apple Watch from Terminating a Session Lock |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_automatic_logout_enforce | Enforce Auto Logout After $ODV Seconds of Inactivity |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_disable | Disable Hot Corners |
| ADDED | system_settings_hot_corners_secure | Secure Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_token_removal_enforce | Configure User Session Lock When a Smart Token is Removed |
| ADDED | system_settings_touch_id_settings_disable | Disable the Touch ID System Settings Pane |
| ADDED | system_settings_touchid_unlock_disable | Disable TouchID for Unlocking the Device |
| ADDED | system_settings_usb_restricted_mode | USB Devices Must be Authorized Before Allowing |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |
| ADDED | system_settings_wifi_disable | Disable Wi-Fi Interface |
| ADDED | system_settings_wifi_disable_when_connected_to_ethernet | Disable Wi-Fi When Connected to Ethernet |

## Rule Changes — Netherlands BIO — Base (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_off_load_records | Off-Load Audit Records |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | os_anti_virus_installed | Must Use an Approved Antivirus Program |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_safari_open_safe_downloads_disable | Disable Automatic Opening of Safe Files in Safari |
| ADDED | os_secure_enclave | Protected Storage for Cryptographic Keys |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_software_update_app_update_enforce | Enforce Software Update App Update Updates Automatically |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_download_software_update_enforce | Enforce Software Update Downloads Updates Automatically using DDM. |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_loginwindow_loginwindowtext_enable | Configure Login Window to Show A Custom Message |
| ADDED | system_settings_macos_updates_install_enforce | Enforce macOS Updates are Automatically Installed using DDM. |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |

## Rule Changes — Netherlands BIO — Plus (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_off_load_records | Off-Load Audit Records |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_anti_virus_installed | Must Use an Approved Antivirus Program |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_external_storage_access_defined | Access to External Storage Must Be Defined |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_install_log_retention_configure | Configure Install.log Retention to $ODV |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_hint_remove | Remove Password Hint From User Accounts |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_provide_automated_account_management | Employ Automated Mechanisms for Account Management Functions |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_advertising_privacy_protection_enable | Ensure Advertising Privacy Protection in Safari Is Enabled |
| ADDED | os_safari_open_safe_downloads_disable | Disable Automatic Opening of Safe Files in Safari |
| ADDED | os_safari_prevent_cross-site_tracking_enable | Ensure Prevent Cross-site Tracking in Safari Is Enabled |
| ADDED | os_safari_show_full_website_address_enable | Ensure Show Full Website Address in Safari Is Enabled |
| ADDED | os_safari_show_status_bar_enabled | Ensure Show Safari shows the Status Bar is Enabled |
| ADDED | os_safari_warn_fraudulent_website_enable | Ensure Warn When Visiting A Fraudulent Website in Safari Is Enabled |
| ADDED | os_secure_boot_verify | Ensure Secure Boot Level Set to Full |
| ADDED | os_secure_enclave | Protected Storage for Cryptographic Keys |
| ADDED | os_setup_assistant_filevault_enforce | Enforce FileVault in Setup Assistant |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_software_update_app_update_enforce | Enforce Software Update App Update Updates Automatically |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudo_timeout_configure | Configure Sudo Timeout Period to $ODV |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_terminal_secure_keyboard_enable | Ensure Secure Keyboard Entry Terminal.app is Enabled |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_background_security_improvement_removal_disable | Disable rollback of Background Security Improvements using DDM. |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_download_software_update_enforce | Enforce Software Update Downloads Updates Automatically using DDM. |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_gatekeeper_identified_developers_allowed | Apply Gatekeeper Settings to Block Applications from Unidentified Developers |
| ADDED | system_settings_gatekeeper_override_disallow | Configure Gatekeeper to Disallow End User Override |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_loginwindow_loginwindowtext_enable | Configure Login Window to Show A Custom Message |
| ADDED | system_settings_macos_updates_install_enforce | Enforce macOS Updates are Automatically Installed using DDM. |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_machine_encrypted_configure | Ensure Time Machine Volumes are Encrypted |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |

## Rule Changes — HICP — Large Healthcare Organizations (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fd_configure | Configure System to Audit All Deletions of Object Attributes |
| ADDED | audit_flags_fm_configure | Configure System to Audit All Changes of Object Attributes |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_certificate_trust_enforce_high | Set Smartcard Certificate Trust to High |
| ADDED | auth_smartcard_certificate_trust_enforce_moderate | Set Smartcard Certificate Trust to Moderate |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_auth_peripherals | Must Authenticate Before Establishing a Connection |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_calendar_app_disable | Disable Calendar.app |
| ADDED | os_certificate_authority_trust | Issue or Obtain Public Key Certificates from an Approved Service Provider |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_erase_content_and_settings_disable | Disable Erase Content and Settings |
| ADDED | os_facetime_app_disable | Disable FaceTime.app |
| ADDED | os_firewall_default_deny_require | Control Connections to Other Systems via a Deny-All and Allow-by-Exception Firewall Policy |
| ADDED | os_firmware_password_require | Enable Firmware Password |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_genmoji_disable | Disable Genmoji AI Creation |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_default | Configure User's Home Folders to Apple's Default |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_image_playground_disable | Disable Apple Intelligence Image Playground |
| ADDED | os_implement_cryptography | Configure the System to Implement Approved Cryptography to Protect Information |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_mail_app_disable | Disable Mail App |
| ADDED | os_mail_smart_reply_disable | Disable Apple Intelligence Mail Smart Replies |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_messages_app_disable | Disable Messages App |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_nonlocal_maintenance | Configure the System for Non-local Maintenance |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_photos_enhanced_search_disable | Disable Photos Enhanced Visual Search |
| ADDED | os_power_nap_disable | Disable Power Nap |
| ADDED | os_privacy_setup_prompt_disable | Disable Privacy Setup Services During Setup Assistant |
| ADDED | os_protect_dos_attacks | Protect Against Denial of Service Attacks by Ensuring Rate-Limiting Measures on Network Interfaces |
| ADDED | os_recovery_lock_enable | Enable Recovery Lock |
| ADDED | os_safari_reader_summary_disable | Disable Apple Intelligence Safari Reader Summary |
| ADDED | os_secure_boot_verify | Ensure Secure Boot Level Set to Full |
| ADDED | os_secure_enclave | Protected Storage for Cryptographic Keys |
| ADDED | os_secure_name_resolution | Secure Name Address Resolution Service |
| ADDED | os_separate_functionality | Configure the System to Separate User and System Functionality |
| ADDED | os_setup_assistant_filevault_enforce | Enforce FileVault in Setup Assistant |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_screen_time_prompt_enable | Disable Screen Time Prompt During Setup Assistant |
| ADDED | os_ssh_fips_compliant | Limit SSH to FIPS Compliant Connections |
| ADDED | os_sshd_fips_compliant | Limit SSHD to FIPS Compliant Connections |
| ADDED | os_sshd_per_source_penalties_configure | Configure SSHD PerSourcePenalties |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_system_read_only | Ensure System Volume is Read Only |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_user_app_installation_prohibit | Prohibit User Installation of Software into /Users/ |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_verify_remote_disconnection | Verify remote disconnection of sessions |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_alpha_numeric_enforce | Require Passwords Contain a Minimum of One Numeric Character |
| ADDED | pwpolicy_custom_regex_enforce | Require Passwords to Match the Defined Custom Regular Expression |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_lower_case_character_enforce | Require Passwords Contain a Minimum of One Lowercase Character |
| ADDED | pwpolicy_max_lifetime_enforce | Restrict Maximum Password Lifetime to $ODV Days |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_minimum_lifetime_enforce | Set Minimum Password Lifetime to $ODV Hours |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | pwpolicy_special_character_enforce | Require Passwords Contain a Minimum of One Special Character |
| ADDED | pwpolicy_upper_case_character_enforce | Require Passwords Contain a Minimum of One Uppercase Character |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_apple_watch_unlock_disable | Prevent Apple Watch from Terminating a Session Lock |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_disable | Disable Location Services |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_ssh_enable | Enable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_touch_id_settings_disable | Disable the Touch ID System Settings Pane |
| ADDED | system_settings_touchid_unlock_disable | Disable TouchID for Unlocking the Device |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |
| ADDED | system_settings_wifi_disable | Disable Wi-Fi Interface |
| ADDED | system_settings_wifi_disable_when_connected_to_ethernet | Disable Wi-Fi When Connected to Ethernet |

## Rule Changes — CIS macOS Benchmark — Level 1 (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_anti_virus_installed | Must Use an Approved Antivirus Program |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_external_apfs_hfs_volumes_encrypted | Ensure All APFS and HFS+ External User Storage Volumes Are Encrypted |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_guest_folder_removed | Remove Guest Folder if Present |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_install_log_retention_configure | Configure Install.log Retention to $ODV |
| ADDED | os_internal_apfs_volumes_encrypted | Ensure All Internal User Storage APFS Volumes Are Encrypted |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_mobile_file_integrity_enable | Enable Apple Mobile File Integrity |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_hint_remove | Remove Password Hint From User Accounts |
| ADDED | os_power_nap_disable | Disable Power Nap |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_advertising_privacy_protection_enable | Ensure Advertising Privacy Protection in Safari Is Enabled |
| ADDED | os_safari_open_safe_downloads_disable | Disable Automatic Opening of Safe Files in Safari |
| ADDED | os_safari_prevent_cross-site_tracking_enable | Ensure Prevent Cross-site Tracking in Safari Is Enabled |
| ADDED | os_safari_show_full_website_address_enable | Ensure Show Full Website Address in Safari Is Enabled |
| ADDED | os_safari_show_status_bar_enabled | Ensure Show Safari shows the Status Bar is Enabled |
| ADDED | os_safari_warn_fraudulent_website_enable | Ensure Warn When Visiting A Fraudulent Website in Safari Is Enabled |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_software_update_app_update_enforce | Enforce Software Update App Update Updates Automatically |
| ADDED | os_software_update_deferral | Ensure Software Update Deferment Is Less Than or Equal to $ODV Days |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudo_timeout_configure | Configure Sudo Timeout Period to $ODV |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_system_wide_applications_configure | Ensure Appropriate Permissions Are Enabled for System Wide Applications |
| ADDED | os_terminal_secure_keyboard_enable | Ensure Secure Keyboard Entry Terminal.app is Enabled |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_world_writable_system_folder_configure | Ensure No World Writable Files Exist in the System Folder |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_max_lifetime_enforce | Restrict Maximum Password Lifetime to $ODV Days |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | supplemental_cis_manual | CIS Manual Recommendations |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_secure | Secure Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_install_macos_updates_enforce | Enforce macOS Updates are Automatically Installed |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_menu_enforce | Ensure Location Services Is In the Menu Bar |
| ADDED | system_settings_loginwindow_loginwindowtext_enable | Configure Login Window to Show A Custom Message |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_software_update_download_enforce | Enforce Software Update Downloads Updates Automatically |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_machine_encrypted_configure | Ensure Time Machine Volumes are Encrypted |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_wake_network_access_disable | Ensure Wake for Network Access Is Disabled |

## Rule Changes — CIS macOS Benchmark — Level 2 (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_anti_virus_installed | Must Use an Approved Antivirus Program |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_external_apfs_hfs_volumes_encrypted | Ensure All APFS and HFS+ External User Storage Volumes Are Encrypted |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_guest_folder_removed | Remove Guest Folder if Present |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_install_log_retention_configure | Configure Install.log Retention to $ODV |
| ADDED | os_internal_apfs_volumes_encrypted | Ensure All Internal User Storage APFS Volumes Are Encrypted |
| ADDED | os_mail_summary_disable | Disable Apple Intelligence Mail Summary |
| ADDED | os_mobile_file_integrity_enable | Enable Apple Mobile File Integrity |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_notes_transcription_disable | Disable Apple Intelligence Notes Transcription |
| ADDED | os_notes_transcription_summary_disable | Disable Apple Intelligence Notes Transcription Summary |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_hint_remove | Remove Password Hint From User Accounts |
| ADDED | os_policy_banner_loginwindow_enforce | Display Policy Banner at Login Window |
| ADDED | os_power_nap_disable | Disable Power Nap |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_advertising_privacy_protection_enable | Ensure Advertising Privacy Protection in Safari Is Enabled |
| ADDED | os_safari_open_safe_downloads_disable | Disable Automatic Opening of Safe Files in Safari |
| ADDED | os_safari_prevent_cross-site_tracking_enable | Ensure Prevent Cross-site Tracking in Safari Is Enabled |
| ADDED | os_safari_show_full_website_address_enable | Ensure Show Full Website Address in Safari Is Enabled |
| ADDED | os_safari_show_status_bar_enabled | Ensure Show Safari shows the Status Bar is Enabled |
| ADDED | os_safari_warn_fraudulent_website_enable | Ensure Warn When Visiting A Fraudulent Website in Safari Is Enabled |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_sleep_and_display_sleep_apple_silicon_enable | Ensure Sleep and Display Sleep Is Enabled on Apple Silicon Devices |
| ADDED | os_software_update_app_update_enforce | Enforce Software Update App Update Updates Automatically |
| ADDED | os_software_update_deferral | Ensure Software Update Deferment Is Less Than or Equal to $ODV Days |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudo_timeout_configure | Configure Sudo Timeout Period to $ODV |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_system_wide_applications_configure | Ensure Appropriate Permissions Are Enabled for System Wide Applications |
| ADDED | os_terminal_secure_keyboard_enable | Ensure Secure Keyboard Entry Terminal.app is Enabled |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_world_writable_library_folder_configure | Ensure No World Writable Files Exist in the Library Folder |
| ADDED | os_world_writable_system_folder_configure | Ensure No World Writable Files Exist in the System Folder |
| ADDED | os_writing_tools_disable | Disable Apple Intelligence Writing Tools |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_alpha_numeric_enforce | Require Passwords Contain a Minimum of One Numeric Character |
| ADDED | pwpolicy_custom_regex_enforce | Require Passwords to Match the Defined Custom Regular Expression |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_max_lifetime_enforce | Restrict Maximum Password Lifetime to $ODV Days |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_special_character_enforce | Require Passwords Contain a Minimum of One Special Character |
| ADDED | supplemental_cis_manual | CIS Manual Recommendations |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_secure | Secure Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_install_macos_updates_enforce | Enforce macOS Updates are Automatically Installed |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_enable | Enable Location Services |
| ADDED | system_settings_location_services_menu_enforce | Ensure Location Services Is In the Menu Bar |
| ADDED | system_settings_loginwindow_loginwindowtext_enable | Configure Login Window to Show A Custom Message |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_password_enforce | Enforce Screen Saver Password |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_software_update_download_enforce | Enforce Software Update Downloads Updates Automatically |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_machine_auto_backup_enable | Configure Time Machine for Automatic Backups |
| ADDED | system_settings_time_machine_encrypted_configure | Ensure Time Machine Volumes are Encrypted |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_wake_network_access_disable | Ensure Wake for Network Access Is Disabled |

## Rule Changes — CIS Controls v8 (macOS 26) — previous → unknown

| Change | Rule ID | Title |
|--------|---------|-------|
| ADDED | audit_acls_files_configure | Configure Audit Log Files to Not Contain Access Control Lists |
| ADDED | audit_acls_folders_configure | Configure Audit Log Folder to Not Contain Access Control Lists |
| ADDED | audit_auditd_enabled | Enable Security Auditing |
| ADDED | audit_control_acls_configure | Configure Audit_Control to Not Contain Access Control Lists |
| ADDED | audit_control_group_configure | Configure Audit_Control Group to Wheel |
| ADDED | audit_control_mode_configure | Configure Audit_Control Owner to Mode 440 or Less Permissive |
| ADDED | audit_control_owner_configure | Configure Audit_Control Owner to Root |
| ADDED | audit_files_group_configure | Configure Audit Log Files Group to Wheel |
| ADDED | audit_files_mode_configure | Configure Audit Log Files to Mode 440 or Less Permissive |
| ADDED | audit_files_owner_configure | Configure Audit Log Files to be Owned by Root |
| ADDED | audit_flags_aa_configure | Configure System to Audit All Authorization and Authentication Events |
| ADDED | audit_flags_ad_configure | Configure System to Audit All Administrative Action Events |
| ADDED | audit_flags_ex_configure | Configure System to Audit All Failed Program Execution on the System |
| ADDED | audit_flags_fm_failed_configure | Configure System to Audit All Failed Change of Object Attributes |
| ADDED | audit_flags_fr_configure | Configure System to Audit All Failed Read Actions on the System |
| ADDED | audit_flags_fw_configure | Configure System to Audit All Failed Write Actions on the System |
| ADDED | audit_flags_lo_configure | Configure System to Audit All Log In and Log Out Events |
| ADDED | audit_folder_group_configure | Configure Audit Log Folders Group to Wheel |
| ADDED | audit_folder_owner_configure | Configure Audit Log Folders to be Owned by Root |
| ADDED | audit_folders_mode_configure | Configure Audit Log Folders to Mode 700 or Less Permissive |
| ADDED | audit_off_load_records | Off-Load Audit Records |
| ADDED | audit_retention_configure | Configure Audit Retention to $ODV |
| ADDED | auth_pam_login_smartcard_enforce | Enforce Multifactor Authentication for Login |
| ADDED | auth_pam_su_smartcard_enforce | Enforce Multifactor Authentication for the su Command |
| ADDED | auth_pam_sudo_smartcard_enforce | Enforce Multifactor Authentication for Privilege Escalation Through the sudo Command |
| ADDED | auth_smartcard_allow | Allow Smartcard Authentication |
| ADDED | auth_smartcard_enforce | Enforce Smartcard Authentication |
| ADDED | auth_ssh_password_authentication_disable | Disable Password Authentication for SSH |
| ADDED | icloud_addressbook_disable | Disable iCloud Address Book |
| ADDED | icloud_appleid_system_settings_disable | Disable the System Setting for Apple ID |
| ADDED | icloud_bookmarks_disable | Disable iCloud Bookmarks |
| ADDED | icloud_calendar_disable | Disable the iCloud Calendar Services |
| ADDED | icloud_drive_disable | Disable iCloud Document Sync |
| ADDED | icloud_freeform_disable | Disable the iCloud Freeform Services |
| ADDED | icloud_game_center_disable | Disable iCloud Game Center |
| ADDED | icloud_keychain_disable | Disable iCloud Keychain Sync |
| ADDED | icloud_mail_disable | Disable iCloud Mail |
| ADDED | icloud_notes_disable | Disable iCloud Notes |
| ADDED | icloud_photos_disable | Disable iCloud Photo Library |
| ADDED | icloud_private_relay_disable | Disable iCloud Private Relay |
| ADDED | icloud_reminders_disable | Disable iCloud Reminders |
| ADDED | icloud_sync_disable | Disable iCloud Desktop and Document Folder Sync |
| ADDED | os_access_control_mobile_devices | Access Control for Mobile Devices |
| ADDED | os_account_modification_disable | Disable AppleID and Internet Account Modifications |
| ADDED | os_airdrop_disable | Disable AirDrop |
| ADDED | os_anti_virus_installed | Must Use an Approved Antivirus Program |
| ADDED | os_appleid_prompt_disable | Disable Apple ID Setup during Setup Assistant |
| ADDED | os_auth_peripherals | Must Authenticate Before Establishing a Connection |
| ADDED | os_authenticated_root_enable | Enable Authenticated Root |
| ADDED | os_bonjour_disable | Disable Bonjour Multicast |
| ADDED | os_config_data_install_enforce | Enforce Installation of XProtect Remediator and Gatekeeper Updates Automatically |
| ADDED | os_dictation_disable | Disable Dictation |
| ADDED | os_directory_services_configured | Integrate System into a Directory Services Infrastructure |
| ADDED | os_ess_installed | Must Use ESS |
| ADDED | os_external_apfs_hfs_volumes_encrypted | Ensure All APFS and HFS+ External User Storage Volumes Are Encrypted |
| ADDED | os_filevault_autologin_disable | Disable FileVault Automatic Login |
| ADDED | os_gatekeeper_enable | Enable Gatekeeper |
| ADDED | os_handoff_disable | Disable Handoff |
| ADDED | os_home_folders_secure | Secure User's Home Folders |
| ADDED | os_httpd_disable | Disable the Built-in Web Server |
| ADDED | os_icloud_storage_prompt_disable | Disable iCloud Storage Setup during Setup Assistant |
| ADDED | os_install_log_retention_configure | Configure Install.log Retention to $ODV |
| ADDED | os_internal_apfs_volumes_encrypted | Ensure All Internal User Storage APFS Volumes Are Encrypted |
| ADDED | os_iphone_mirroring_disable | Disable iPhone Mirroring |
| ADDED | os_ir_support_disable | Disable Infrared (IR) support |
| ADDED | os_library_validation_enabled | Enable Library Validation |
| ADDED | os_logical_access | Enforce Approved Authorization for Logical Access |
| ADDED | os_malicious_code_prevention | Ensure the System Implements Malicious Code Protection Mechanisms |
| ADDED | os_mdm_require | Enforce Enrollment in Mobile Device Management |
| ADDED | os_mfa_network_access | Enforce multifactor authentication for network access to privileged accounts |
| ADDED | os_mobile_file_integrity_enable | Enable Apple Mobile File Integrity |
| ADDED | os_nfsd_disable | Disable Network File System Service |
| ADDED | os_obscure_password | Obscure Passwords |
| ADDED | os_on_device_dictation_enforce | Enforce On Device Dictation |
| ADDED | os_password_hint_remove | Remove Password Hint From User Accounts |
| ADDED | os_password_proximity_disable | Disable Proximity Based Password Sharing Requests |
| ADDED | os_password_sharing_disable | Disable Password Sharing |
| ADDED | os_power_nap_disable | Disable Power Nap |
| ADDED | os_privacy_setup_prompt_disable | Disable Privacy Setup Services During Setup Assistant |
| ADDED | os_root_disable | Disable Root Login |
| ADDED | os_safari_advertising_privacy_protection_enable | Ensure Advertising Privacy Protection in Safari Is Enabled |
| ADDED | os_safari_open_safe_downloads_disable | Disable Automatic Opening of Safe Files in Safari |
| ADDED | os_safari_prevent_cross-site_tracking_enable | Ensure Prevent Cross-site Tracking in Safari Is Enabled |
| ADDED | os_safari_show_full_website_address_enable | Ensure Show Full Website Address in Safari Is Enabled |
| ADDED | os_safari_show_status_bar_enabled | Ensure Show Safari shows the Status Bar is Enabled |
| ADDED | os_safari_warn_fraudulent_website_enable | Ensure Warn When Visiting A Fraudulent Website in Safari Is Enabled |
| ADDED | os_secure_name_resolution | Secure Name Address Resolution Service |
| ADDED | os_setup_assistant_filevault_enforce | Enforce FileVault in Setup Assistant |
| ADDED | os_sip_enable | Ensure System Integrity Protection is Enabled |
| ADDED | os_siri_prompt_disable | Disable Siri Setup during Setup Assistant |
| ADDED | os_skip_apple_intelligence_enable | Disable Apple Intelligence During Setup Assistant |
| ADDED | os_skip_unlock_with_watch_enable | Disable Unlock with Apple Watch During Setup Assistant |
| ADDED | os_sleep_and_display_sleep_apple_silicon_enable | Ensure Sleep and Display Sleep Is Enabled on Apple Silicon Devices |
| ADDED | os_software_update_app_update_enforce | Enforce Software Update App Update Updates Automatically |
| ADDED | os_store_encrypted_passwords | Encrypt Stored Passwords |
| ADDED | os_sudo_log_enforce | Configure Sudo To Log Events |
| ADDED | os_sudo_timeout_configure | Configure Sudo Timeout Period to $ODV |
| ADDED | os_sudoers_timestamp_type_configure | Configure Sudoers Timestamp Type |
| ADDED | os_system_wide_applications_configure | Ensure Appropriate Permissions Are Enabled for System Wide Applications |
| ADDED | os_terminal_secure_keyboard_enable | Ensure Secure Keyboard Entry Terminal.app is Enabled |
| ADDED | os_tftpd_disable | Disable Trivial File Transfer Protocol Service |
| ADDED | os_time_server_enabled | Enable Time Synchronization Daemon |
| ADDED | os_touchid_prompt_disable | Disable TouchID Prompt during Setup Assistant |
| ADDED | os_unique_identification | Uniquely Identify Users and Processes |
| ADDED | os_unlock_active_user_session_disable | Disable Login to Other User's Active and Locked Sessions |
| ADDED | os_uucp_disable | Disable Unix-to-Unix Copy Protocol Service |
| ADDED | os_world_writable_library_folder_configure | Ensure No World Writable Files Exist in the Library Folder |
| ADDED | os_world_writable_system_folder_configure | Ensure No World Writable Files Exist in the System Folder |
| ADDED | pwpolicy_account_inactivity_enforce | Disable Accounts after $ODV Days of Inactivity |
| ADDED | pwpolicy_account_lockout_enforce | Limit Consecutive Failed Login Attempts to $ODV |
| ADDED | pwpolicy_account_lockout_timeout_enforce | Set Account Lockout Time to $ODV Minutes |
| ADDED | pwpolicy_alpha_numeric_enforce | Require Passwords Contain a Minimum of One Numeric Character |
| ADDED | pwpolicy_custom_regex_enforce | Require Passwords to Match the Defined Custom Regular Expression |
| ADDED | pwpolicy_force_password_change | Force Password Change at Next Logon |
| ADDED | pwpolicy_history_enforce | Prohibit Password Reuse for a Minimum of $ODV Generations |
| ADDED | pwpolicy_max_lifetime_enforce | Restrict Maximum Password Lifetime to $ODV Days |
| ADDED | pwpolicy_minimum_length_enforce | Require a Minimum Password Length of $ODV Characters |
| ADDED | pwpolicy_minimum_lifetime_enforce | Set Minimum Password Lifetime to $ODV Hours |
| ADDED | pwpolicy_simple_sequence_disable | Prohibit Repeating, Ascending, and Descending Character Sequences |
| ADDED | pwpolicy_special_character_enforce | Require Passwords Contain a Minimum of One Special Character |
| ADDED | supplemental_filevault | FileVault Supplemental |
| ADDED | supplemental_password_policy | Password Policy Supplemental |
| ADDED | system_settings_airplay_receiver_disable | Disable Airplay Receiver |
| ADDED | system_settings_automatic_login_disable | Disable Unattended or Automatic Logon to the System |
| ADDED | system_settings_bluetooth_disable | Disable Bluetooth When no Approved Device is Connected |
| ADDED | system_settings_bluetooth_menu_enable | Enable Bluetooth Menu |
| ADDED | system_settings_bluetooth_settings_disable | Disable the Bluetooth System Settings Pane |
| ADDED | system_settings_bluetooth_sharing_disable | Disable Bluetooth Sharing |
| ADDED | system_settings_content_caching_disable | Disable Content Caching Service |
| ADDED | system_settings_critical_update_install_enforce | Enforce Critical Security Updates to be Installed |
| ADDED | system_settings_diagnostics_reports_disable | Disable Sending Diagnostic and Usage Data to Apple |
| ADDED | system_settings_download_software_update_enforce | Enforce Software Update Downloads Updates Automatically using DDM. |
| ADDED | system_settings_external_intelligence_disable | Disable External Intelligence Integrations |
| ADDED | system_settings_external_intelligence_sign_in_disable | Disable External Intelligence Integration Sign In |
| ADDED | system_settings_filevault_enforce | Enforce FileVault |
| ADDED | system_settings_find_my_disable | Disable Find My Service |
| ADDED | system_settings_firewall_enable | Enable macOS Application Firewall |
| ADDED | system_settings_firewall_stealth_mode_enable | Enable Firewall Stealth Mode |
| ADDED | system_settings_guest_access_smb_disable | Disable Guest Access to Shared SMB Folders |
| ADDED | system_settings_guest_account_disable | Disable the Guest Account |
| ADDED | system_settings_hot_corners_secure | Secure Hot Corners |
| ADDED | system_settings_improve_assistive_voice_disable | Disable Sending Audio Recordings and Transcripts to Apple |
| ADDED | system_settings_improve_search_disable | Disable Improve Search Information to Apple |
| ADDED | system_settings_improve_siri_dictation_disable | Disable Improve Siri and Dictation Information to Apple |
| ADDED | system_settings_install_macos_updates_enforce | Enforce macOS Updates are Automatically Installed |
| ADDED | system_settings_internet_accounts_disable | Disable the Internet Accounts System Preference Pane |
| ADDED | system_settings_internet_sharing_disable | Disable Internet Sharing |
| ADDED | system_settings_location_services_enable | Enable Location Services |
| ADDED | system_settings_loginwindow_loginwindowtext_enable | Configure Login Window to Show A Custom Message |
| ADDED | system_settings_loginwindow_prompt_username_password_enforce | Configure Login Window to Prompt for Username and Password |
| ADDED | system_settings_media_sharing_disabled | Disable Media Sharing |
| ADDED | system_settings_password_hints_disable | Disable Password Hints |
| ADDED | system_settings_personalized_advertising_disable | Disable Personalized Advertising |
| ADDED | system_settings_printer_sharing_disable | Disable Printer Sharing |
| ADDED | system_settings_rae_disable | Disable Remote Apple Events |
| ADDED | system_settings_remote_management_disable | Disable Remote Management |
| ADDED | system_settings_screen_sharing_disable | Disable Screen Sharing and Apple Remote Desktop |
| ADDED | system_settings_screensaver_ask_for_password_delay_enforce | Enforce Session Lock After Screen Saver is Started |
| ADDED | system_settings_screensaver_timeout_enforce | Enforce Screen Saver Timeout |
| ADDED | system_settings_security_update_install | Enforce Automatic Installs of Available Security Updates using DDM. |
| ADDED | system_settings_siri_disable | Disable Siri |
| ADDED | system_settings_siri_listen_disable | Ensure Siri Listen For is Disabled |
| ADDED | system_settings_siri_settings_disable | Disable the System Settings Pane for Siri |
| ADDED | system_settings_smbd_disable | Disable Server Message Block Sharing |
| ADDED | system_settings_software_update_download_enforce | Enforce Software Update Downloads Updates Automatically |
| ADDED | system_settings_softwareupdate_current | Ensure Software Update is Updated and Current |
| ADDED | system_settings_ssh_disable | Disable SSH Server for Remote Access Sessions |
| ADDED | system_settings_system_wide_preferences_configure | Require Administrator Password to Modify System-Wide Preferences |
| ADDED | system_settings_time_machine_auto_backup_enable | Configure Time Machine for Automatic Backups |
| ADDED | system_settings_time_machine_encrypted_configure | Ensure Time Machine Volumes are Encrypted |
| ADDED | system_settings_time_server_configure | Configure macOS to Use an Authorized Time Server |
| ADDED | system_settings_time_server_enforce | Enforce macOS Time Synchronization |
| ADDED | system_settings_touch_id_settings_disable | Disable the Touch ID System Settings Pane |
| ADDED | system_settings_wake_network_access_disable | Ensure Wake for Network Access Is Disabled |
| ADDED | system_settings_wallet_applepay_settings_disable | Disable the System Settings Pane for Wallet and Apple Pay |
| ADDED | system_settings_wifi_disable | Disable Wi-Fi Interface |
| ADDED | system_settings_wifi_menu_enable | Enable Wifi Menu |

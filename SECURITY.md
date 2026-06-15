# Security Policy

## Reporting a Vulnerability

If you discover a security issue in these modules (e.g., a misconfigured security control that weakens a macOS security posture, or a pipeline vulnerability), please report it privately:

1. **DO NOT** open a public issue
2. Email security@your-org.com with details
3. Include: affected module, version, description, reproduction steps

## Scope

Security issues include:
- Incorrect compliance rule mappings (rule says "enforce screensaver" but generates "allow screensaver disable")
- Missing rules from a baseline
- Pipeline vulnerabilities (workflow injection, secret exposure)
- Exemption bypass (exemption processing logic allows rules to be silently skipped)

## Out of scope

- Issues in upstream NIST mSCP rules (report to https://github.com/usnistgov/macos_security)
- Issues in Jamf Platform or Jamf Pro (report to Jamf support)
- Issues in Terraform providers (report to respective provider repositories)

## Supported versions

Only the latest tagged release is supported. Generated modules track mSCP versions; always use the latest.

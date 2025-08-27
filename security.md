# Security

## Threat Model (STRIDE)
- **Spoofing**: mitigated via GitHub OIDC tokens.
- **Tampering**: code signing with cosign.
- **Repudiation**: signed audit logs stored for 90 days.
- **Information Disclosure**: least-privilege tokens and secret scanning.
- **Denial of Service**: rate limits on webhooks.
- **Elevation of Privilege**: minimal runner permissions.

## Secret Management
- Secrets sourced from environment variables provided by GitHub Actions.
- Rotation policy: quarterly via repository settings.

## SBOM
- Generated with `syft . -o json > sbom.json`.
- Policy: fail pipeline on critical vulnerabilities using `grype sbom.json`.

## Data Handling
| Data | Retention | Location |
|------|-----------|----------|
| Logs | 30 days   | GitHub Actions | 
| Test Reports | 30 days | GitHub Artifacts |

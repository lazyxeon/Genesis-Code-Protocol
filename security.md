# Security & Supply Chain

## Threat Model (STRIDE)

- **Spoofing**: OIDC tokens required for CLI and HTTP calls.
- **Tampering**: Scan reports and SBOM signed with Sigstore.
- **Repudiation**: All scan invocations logged with request ID.
- **Information Disclosure**: Secrets stored in GitHub Actions secrets; results contain no secrets.
- **Denial of Service**: Rate limiting 60 req/min and job timeouts.
- **Elevation of Privilege**: GitHub token scoped to read security events.

## Secret Management

Secrets are sourced from environment variables:
- `CODACY_PROJECT_TOKEN`
- `FOD_TENANT`, `FOD_USER`, `FOD_PAT`
- `SSC_TOKEN`, `SC_CLIENT_AUTH_TOKEN`, `DEBRICKED_TOKEN`

Rotation occurs every 90 days via platform automation.

## SBOM

Generate SBOM with:
```bash
syft . -o json > sbom.json
```
Fail the pipeline on critical vulnerabilities.

## Data Handling & Retention

| Data            | Retention | Notes                       |
|-----------------|-----------|-----------------------------|
| Scan Reports    | 90 days   | Stored in internal bucket   |
| Workflow Logs   | 30 days   | PII scrubbed                |

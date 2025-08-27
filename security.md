# Security & Supply Chain

## Threat Model (STRIDE)
- **Spoofing**: OIDC tokens validated against issuer.
- **Tampering**: Artifacts signed via Sigstore.
- **Repudiation**: Audit logs stored for 90 days.
- **Information Disclosure**: Secrets loaded from env vars; no secrets logged.
- **Denial of Service**: Rate limiting on HTTP and queue consumers.
- **Elevation of Privilege**: Least-privilege IAM for `workflow-sa`.

## Secret Management
- `CI_WORKFLOW_DIAGNOSER_TOKEN` sourced from environment variables.
- Rotation every 90 days via secrets manager.

## SBOM
```
syft . -o json > sbom.json
```
Policy: fail build on critical vulnerabilities.

## Data Handling
| Data | Location | Retention |
|------|----------|-----------|
| Logs | object storage | 30 days |
| Reports | `dist/` | 90 days |

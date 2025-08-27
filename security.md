# Security & Supply Chain

## Threat Model (STRIDE)

- **Spoofing**: OIDC authentication enforced for API calls.
- **Tampering**: Artifacts signed with Sigstore; SBOM verified.
- **Repudiation**: Audit logs stored for 90 days.
- **Information Disclosure**: `GITHUB_TOKEN` kept in secret store.
- **Denial of Service**: Rate limiting at 60 req/min.
- **Elevation of Privilege**: Token scoped read-only.

## Secret Management

`GITHUB_TOKEN` sourced from environment; rotated every 90 days.

## SBOM

Generated via `syft . -o json > sbom.json`. Pipeline fails on critical vulnerabilities.

## Data Handling & Retention

| Data              | Retention | Notes                     |
|-------------------|-----------|---------------------------|
| Stability Reports | 90 days   | Stored in internal bucket |
| Workflow Logs     | 30 days   | Redacted for PII          |

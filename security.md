# Security

## Threat Model (STRIDE)
- **Spoofing**: OIDC-issued tokens for all requests.
- **Tampering**: Artifacts signed and SBOM verified.
- **Repudiation**: Immutable audit logs stored for 90 days.
- **Information Disclosure**: Secrets kept out of logs; data classified as internal.
- **Denial of Service**: Rate limits on HTTP interface.
- **Elevation of Privilege**: Least-privilege IAM for `workflow-sa`.

## Secrets
- `REGISTRY_TOKEN` sourced from environment variables or vault and rotated every 90 days.

## SBOM
- `syft . -o json > sbom.json`
- Build fails on critical vulnerabilities.

## Data Handling
| data | retention_days | location |
| --- | --- | --- |
| build_logs | 30 | s3://build-logs |
| artifacts | 90 | registry |

# Security and Supply Chain

## Threat Model (STRIDE)
| Threat | Mitigation |
|--------|------------|
| Spoofing | OIDC tokens for all interfaces |
| Tampering | Signed artifacts using sigstore |
| Repudiation | Audit logs with immutable storage |
| Information Disclosure | Data classified as internal, encrypted at rest |
| Denial of Service | Rate limits and exponential backoff |
| Elevation of Privilege | Least-privilege service account |

## Secret Management
- Secrets provided via environment variables (`ENV:TRIVY_DB_TOKEN`).
- Rotated every 90 days via vault automation.

## SBOM
```bash
syft . -o json > sbom.json
```
Policy: build fails if any critical vulnerability is found.

## Data Handling & Retention
| Data | Location | Retention |
|------|----------|-----------|
| Source Archive | ephemeral container FS | deleted after run |
| Reports | s3://reports | 90 days |

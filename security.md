<<<<<< codex/develop-fuzzing-and-vulnerability-scanning-workflow
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
=======
# Security & Supply Chain

## Threat Model (STRIDE)
- **Spoofing**: Mitigated via OIDC authentication.
- **Tampering**: Artifacts signed with Sigstore.
- **Repudiation**: Audit logs stored for 90 days.
- **Information Disclosure**: Secrets stored in GitHub Actions secrets.
- **Denial of Service**: Rate limiting at 60 req/min.
- **Elevation of Privilege**: Least-privilege GitHub token.

## Secret Management
`SECURE_REPO_TOKEN` sourced from environment; rotated every 90 days.

## SBOM
Generated via `syft . -o json > sbom.json`. Pipeline fails on critical vulnerabilities.

## Data Handling & Retention
| Data | Retention | Notes |
|------|-----------|-------|
| Scorecard Reports | 30 days | Stored in internal bucket |
| Remediation PRs | 90 days | GitHub retains metadata |
>>>>>> main

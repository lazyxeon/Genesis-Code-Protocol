<<<<<< codex/develop-and-implement-matrix-ci
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
=======
<<<<<< codex/analyze-failing-github-workflows
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
=======
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
>>>>>> main
>>>>>> main

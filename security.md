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

| Data              | Retention | Notes                     |
|-------------------|-----------|---------------------------|
| Scorecard Reports | 30 days   | Stored in internal bucket |
| Remediation PRs   | 90 days   | GitHub retains metadata   |

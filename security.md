# Security

## Threat Model (STRIDE)
- **Spoofing**: Require token-based auth; validate Dependabot author.
- **Tampering**: Use signed commits and protected branches.
- **Repudiation**: Audit logs via GitHub API.
- **Information Disclosure**: Secrets stored in GitHub Actions secrets.
- **Denial of Service**: Rate limiting and retries.
- **Elevation of Privilege**: Least-privilege `GITHUB_TOKEN`.

## Secret Sourcing
- `GITHUB_TOKEN` from GitHub Actions; rotate daily.

## SBOM
`syft . -o json > sbom.json`
Policy: fail on critical vulnerabilities.

## Data Handling & Retention
| Data        | Retention | Notes |
|-------------|-----------|-------|
| automerge_report | 90 days  | stored in artifact storage |

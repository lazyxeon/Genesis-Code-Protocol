# Security and Supply Chain

## Threat Model (STRIDE)
- **Spoofing**: GitHub webhook signatures verified (`X-Hub-Signature-256`).
- **Tampering**: Containers signed with cosign; SBOM policy fails on critical findings.
- **Repudiation**: All steps emit JSON logs with trace IDs.
- **Information Disclosure**: secrets stored in `ENV:PYPI_TOKEN`, rotated monthly.
- **Denial of Service**: Rate limits enforced at HTTP and queue layers.
- **Elevation of Privilege**: Workflow runs with least-privilege `workflow-sa` IAM role.

## Secret Management
- Sourced from environment variables or vault references.
- Rotation policy: monthly or on incident.

## SBOM Generation
```bash
syft . -o json > sbom.json
```
Policy: pipeline fails on critical vulnerabilities.

## Data Handling & Retention
| Data Type    | Location   | Retention |
|--------------|------------|-----------|
| test_report  | artifact store | 30 days |
| logs         | log backend | 90 days |
| sbom.json    | artifact store | 90 days |

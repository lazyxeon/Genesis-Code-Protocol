# Security & Supply Chain

## Threat Model (STRIDE)

- **Spoofing**: OIDC authentication ensures only trusted runners trigger workflow steps.
- **Tampering**: Release bundles and SBOMs are signed via Sigstore.
- **Repudiation**: Every step logs an `X-Request-ID` and trace span.
- **Information Disclosure**: Secrets stored in Actions secrets; reports contain no secrets.
- **Denial of Service**: Concurrency guards and rate limits mitigate overload.
- **Elevation of Privilege**: `GITHUB_TOKEN` scoped to repository content only.

## Secret Management

Secrets are provided via environment variables:

- `GITHUB_TOKEN`
- `COSIGN_EXPERIMENTAL`

Rotation occurs every 90 days through the secrets manager.

## SBOM

Generate SBOM with:

```bash
syft . -o json > sbom.json
```

Policy: fail the pipeline on critical vulnerabilities.

## Data Handling & Retention

| Data         | Retention | Notes                    |
|--------------|-----------|--------------------------|
| CI Report    | 90 days   | Stored in internal bucket |
| Workflow Logs| 30 days   | PII scrubbed              |

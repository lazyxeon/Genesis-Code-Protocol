# Integration Contract: secure-repo-scorecard-remediation

## Interfaces

### CLI

```bash
python -m src.scan --repo <owner/repo>
python -m src.remediate --report report.json
```

### HTTP

`POST /remediate` with body `{ "repo": "owner/repo" }`

### Webhook

GitHub `pull_request` events trigger remediation.

### Queue

Messages on `secure-repo-remediation` queue follow schema:

```json
{
  "repo": "owner/repo",
  "commit": "sha",
  "action": "scan|remediate"
}
```

## Authentication

- CLI: OIDC token via `SECURE_REPO_TOKEN`.
- HTTP/Queue: Bearer token in `Authorization` header.

Rate limit: 60 req/min per repo.

All requests must include an `X-Request-ID` header for traceability.

Error shape:

```json
{ "error": "string", "retry": true }
```

## Idempotency

Idempotency key = SHA256 of repo and commit. Duplicate keys are ignored.

## Versioning

Semantic versioning with 6-month deprecation window. Backward compatibility tests run via `tests/contract.test.py`.

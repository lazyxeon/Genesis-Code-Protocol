# Integration Contract: security-scan-workflow

## Interfaces

### CLI

```bash
python -m src.main --repo <owner/repo>
```

### HTTP

`POST /security/scan` with body `{ "repo": "owner/repo" }`

### Webhook

GitHub `workflow_run` events trigger scanning.

### Queue

Messages on `security-scan` queue follow schema:

```json
{
  "repo": "owner/repo",
  "commit": "sha",
  "action": "scan"
}
```

## Authentication

- CLI/HTTP/Queue: Bearer token via `GITHUB_TOKEN` or OIDC.
- Rate limit: 60 req/min per repo.
- All requests must include `X-Request-ID` header.

Error shape:

```json
{"error": "string", "request_id": "uuid"}
```

## Idempotency

- Idempotency key is the commit SHA.
- Re-sending with same key overwrites previous results.

## Versioning

- Semantic versioning (`1.0.0`).
- Deprecation window: 90 days after minor release.
- Backward compatibility tests verify previous contract versions.

## Compatibility Tests

- `tests/contract_test.py` exercises authentication and idempotency.
- CI runs these on every pull request.

# Integration Contract: github-actions-stability

## Interfaces

### CLI

```bash
python -m src.main --repo <owner/repo>
```

### HTTP

`POST /stability` with body `{ "repo": "owner/repo" }`

### Webhook

GitHub `workflow_run` events trigger analysis.

### Queue

Messages on `gha-stability` queue follow schema:

```json
{
  "repo": "owner/repo",
  "branch": "main",
  "commit": "sha",
  "action": "analyze"
}
```

## Authentication

- CLI/HTTP/Queue: Bearer token via `GITHUB_TOKEN`.
- All requests must include an `X-Request-ID` header.
- Rate limit: 60 req/min per repo.

Error shape:

```json
{ "error": "string", "retry": true }
```

## Idempotency

Idempotency key = SHA256 of repo and commit. Duplicate keys are ignored.

## Versioning

Semantic versioning with 6-month deprecation window. Backward compatibility tests run via `tests/test_contract.py`.

# Integration Contract: gha-workflow-resilience

## Interfaces

### CLI

```bash
python -m src.resilience run --repo <owner/repo> --tag v1.2.3
```

### HTTP

`POST /workflows/resilience` with body `{"repo":"owner/repo","tag":"v1.2.3"}`

### Webhook

GitHub `push` and `release` events trigger the workflow via Actions dispatch.

### Queue

Messages on `workflow-resilience` queue follow schema:

```json
{
  "repo": "owner/repo",
  "tag": "v1.2.3",
  "action": "run"
}
```

### GitHub Actions

Manual dispatch via API:

```bash
curl -X POST \
  -H "Authorization: Bearer <token>" \
  https://api.github.com/repos/<owner>/<repo>/actions/workflows/gha-workflow-resilience.yml/dispatches \
  -d '{"ref":"main","inputs":{"tag":"v1.2.3"}}'
```

## Authentication

- Bearer token (`GITHUB_TOKEN`) or OIDC.
- Rate limit: 60 req/min per repo.
- All requests include `X-Request-ID` header.

Error shape:

```json
{"error":"string","request_id":"uuid"}
```

## Idempotency

- Idempotency key: `<repo>#<tag>`.
- Replays with same key overwrite prior artifacts.

## Versioning

- Semantic versioning (`1.0.0`).
- Deprecation window: 90 days after minor release.
- Backward/forward compatibility tests ensure contract stability.

## Compatibility Tests

- `tests/contract_test.py` exercises authentication and idempotency rules.

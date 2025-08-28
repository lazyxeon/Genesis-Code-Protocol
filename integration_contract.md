# Dependabot Auto-merge Integration Contract

## Interfaces
- **CLI**: `python -m src.automerge --pr <num> --repo <owner/repo>`
- **HTTP**: `POST /automerge` with JSON `{ "pr": <num>, "repo": "<owner/repo>" }`

### Example (HTTP)

```bash
curl -H "Authorization: Bearer $TOKEN" \
     -H "X-Request-ID: <uuid>" \
     -d '{"pr":123,"repo":"octo/repo"}' \
     https://example.com/automerge
```

## Authentication
Bearer token via `Authorization` header or `GITHUB_TOKEN` env var.
Rate limit: 60 req/min per repo.

## Idempotency
`X-Request-ID` required. Replays with same ID are ignored.

## Versioning
Semantic versioning. Deprecation window: 6 months after minor release.

## Errors
- `401 Unauthorized`
- `404 Not Found`
- `409 Conflict` when PR not authored by Dependabot

<<<<<< codex/develop-fuzzing-and-vulnerability-scanning-workflow
# Fuzzing and Vulnerability Scanning Workflow Integration Contract

## Interfaces

### CLI
```bash
# Run a full fuzz and scan cycle
env WF_SOURCE_ARCHIVE=src.tar.gz python -m src.main
```

### HTTP
- **POST** `/run`
  - Body: `{ "source_archive": "base64(tar.gz)" }`
  - Response: `{ "report_url": "s3://reports/<id>.json" }`

### Webhook
- Optional webhook can be configured to receive `{ "status": "complete", "report_url": "..." }`.

### Queue
- Messages on `fuzzing_vuln_scan.jobs` queue trigger runs with payload identical to HTTP body.

## Authentication
- All interfaces require `Bearer` token from OIDC provider.
- CLI expects token in `ENV:WF_AUTH_TOKEN`.
- HTTP uses `Authorization: Bearer <token>` header.
- Rate limit: 60 runs/min per token.
- Error shape:
```json
{ "error": { "code": "string", "message": "string" } }
```

## Idempotency
- `X-Idempotency-Key` header (HTTP/Queue) or `--idempotency-key` flag (CLI).
- Replays with same key return cached report without rerunning steps.

## Versioning
- Semantic Versioning for workflow (`1.0.0`).
- Deprecation window: 6 months after new major release; old endpoints continue to serve but emit warning header `Deprecated: <date>`.
- Backward compatibility tests ensure old clients operate until window expires.

## Compatibility Tests
- `tests/contract.test.py` covers interface schemas, auth failure paths, and idempotency handling.
=======
# Integration Contract: secure-repo-scorecard-remediation

## Interfaces
### CLI
```
$ python -m src.scan --repo <owner/repo>
$ python -m src.remediate --report report.json
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

Error shape:
```json
{ "error": "string", "retry": true }
```

## Idempotency
Idempotency key = SHA256 of repo and commit. Duplicate keys are ignored.

## Versioning
Semantic Versioning with 6-month deprecation window.
Backward compatibility tests run via `tests/contract.test.py`.
>>>>>> main

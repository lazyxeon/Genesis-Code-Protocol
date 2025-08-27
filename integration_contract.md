# Matrix CI Pipeline Integration Contract

## Interfaces

### CLI
- `make test` — runs lint and unit tests.
- `make sbom` — generates an SBOM using Syft.

### HTTP
- Webhook: `POST /ci/event` receives GitHub push events.
- Example payload:
```json
{ "ref": "refs/heads/main", "commit": "<sha>" }
```

### Queue
- Jobs are enqueued on the GitHub Actions runner queue with the matrix of Python versions.

## Authentication
- CLI commands run locally and require no authentication.
- HTTP webhook requires a GitHub shared secret via `X-Hub-Signature-256`.
- Queue access uses GitHub OIDC tokens scoped to the repository.

## Rate Limits
- Webhook: 100 requests/minute per source IP.
- Queue: maximum 20 concurrent jobs.

## Error Shapes
```json
{ "error": "string", "retryable": true, "details": {} }
```

## Idempotency
- Requests identified by commit SHA; duplicate events with same SHA are ignored.

## Versioning
- SemVer with MAJOR.MINOR.PATCH.
- Deprecation window: 6 months after announcing a breaking change.

## Compatibility Tests
- `tests/contract_test.py` ensures this document is current.
- Backward and forward compatibility verified through GitHub Actions smoke tests.

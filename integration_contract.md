# Integration Contract: matrix-ci-repair

## Interfaces
### CLI
```bash
make test          # run lint and unit tests
make sbom          # generate SBOM with Syft
```

### HTTP
- **Endpoint**: `POST /ci/event`
- **Request**:
```json
{ "ref": "refs/heads/main", "commit": "<sha>" }
```
- **Response**:
```json
{ "status": "queued", "id": "<uuid>" }
```

### Queue
- **Name**: `matrix-ci-jobs`
- **Message Schema**: `{ "id": "<uuid>", "python": "3.11", "commit": "<sha>" }`

## Authentication
- Webhook requests must include `X-Hub-Signature-256` header.
- Queue consumers authenticate with GitHub OIDC tokens.
- CLI runs locally without additional auth.

## Rate Limits
- HTTP: 100 requests/minute per source IP.
- Queue: 20 concurrent jobs.

## Error Shapes
```json
{ "error": "string", "retryable": true, "details": {} }
```

## Idempotency
- Deduplication key is commit SHA; duplicate events with the same SHA are ignored.

## Versioning
- Semantic Versioning (MAJOR.MINOR.PATCH).
- Deprecation window: 6 months after announcing a breaking change.

## Compatibility Tests
- `tests/contract.test.py` asserts presence of required sections.
- Nightly builds run contract tests against previous release to ensure backward compatibility.

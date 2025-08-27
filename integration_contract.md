# Integration Contract: CI Workflow Diagnoser

## Interfaces

### CLI
```
python -m src.ingest --input logs.json --output report.json
```

### HTTP
- **Endpoint**: `POST /diagnose`
- **Request Body**: JSON workflow logs
- **Response**: JSON diagnosis report

### Queue
- **Queue Name**: `ci-workflow-jobs`
- Messages contain a pointer to log payloads stored in object storage.

## Authentication
- Bearer tokens via `Authorization` header for HTTP.
- OIDC tokens for queue consumers.
- CLI reads token from `CI_WORKFLOW_DIAGNOSER_TOKEN`.

## Rate Limits
- HTTP: 60 requests/minute per token.
- Queue: 100 messages/minute.

## Error Handling
- 400: invalid input schema
- 401: unauthorized
- 500: internal error

## Idempotency
Requests include an `X-Request-ID` header; duplicate IDs return the original result.

## Versioning
- Semantic versioning (MAJOR.MINOR.PATCH)
- Deprecated versions supported for 180 days

## Compatibility Tests
- Backward compatibility: run against previous N-1 release.
- Forward compatibility: contract tests executed in nightly builds.

# Build Pipeline Stabilizer Integration Contract

## Interfaces

### CLI
- `python -m src.main --input <file> --workdir <dir>` – run full pipeline.
- `python -m src.ingest --input <file> --output <file>` – normalize records.

### HTTP
- `POST /build` with JSON `{ "repo": "url" }` triggers build. Response: `{ "image": "registry/ref" }`.

### Webhook
- `POST /events/push` from Git provider initiates pipeline.

## Authentication
- CLI: environment variable `REGISTRY_TOKEN` for push.
- HTTP/Webhook: bearer token in `Authorization` header.
- Tokens issued via OIDC with 1h expiry.

## Rate Limits
- 60 build requests per hour; excess receives `429` with `Retry-After` header.

## Errors
- Errors use shape `{ "error": {"code": <string>, "message": <string> } }`.

## Idempotency
- `X-Idempotency-Key` header ensures deduplication; repeated requests with same key return original response.

## Versioning
- Semantic Versioning. Current version: `v1`.
- Deprecation window: 6 months after new major release.

## Compatibility Tests
- Backward: run `tests/*` against previous `v1` artifacts.
- Forward: nightly pipeline runs contract tests against `main` branch.

# Integration Contract

## Interfaces
Supports CLI and HTTP interfaces for invoking the workflow.

## Authentication
Requests must include a bearer token.

## Idempotency
Clients supply an `X-Request-ID` header to ensure duplicate submissions are ignored.

## Versioning
Semantic versioning is used; one minor version is supported before deprecation.

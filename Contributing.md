# Contributing to Genesis Code Protocol

Thanks for your interest in GCP! We welcome improvements to code, docs, and protocols.

## Quick Start

1. **Fork** the repo and create a branch: `git checkout -b feat/<topic>`  
2. **Set up**: Python 3.10+, `pip install -r requirements.txt`  
3. **Run checks**: lint/format/tests as provided (see CI config)  
4. **Open a PR** with a clear description and checklist (see template)

## Development Guidelines

- Follow Python best practices (typing, docstrings, tests).  
- Keep PRs focused and small; link related issues.  
- Explain **protocol impacts**: gates affected, artifacts updated, risk tier if applicable.  
- Update docs/notebooks when behavior or public surfaces change.

## Commit & PR Style

- Conventional commits recommended: `docs: …`, `feat: …`, `fix: …`, `refactor: …`.  
- PRs must pass CI (build/tests/linters/security scans) and include relevant docs/CHANGELOG updates.

## Versioning & Compatibility

- Use SemVer for public surfaces; run **compatibility tests** before merging.  
- Breaking changes require a major bump and deprecation guidance.

## Code of Conduct

By participating, you agree to our [Code of Conduct](../CODE_OF_CONDUCT.md).

## Security

Please **do not** file public issues for vulnerabilities. Follow our [Security Policy](../SECURITY.md).

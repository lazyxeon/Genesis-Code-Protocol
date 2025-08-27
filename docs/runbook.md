# GitHub Actions Stability Runbook

## Overview

This runbook guides operators through running and troubleshooting the workflow that analyzes GitHub Actions runs to detect failing workflows.

## Normal Operation

1. Ensure `GITHUB_TOKEN` is set in the environment.
2. Execute `make install` to install dependencies.
3. Run `make test` to verify the workflow passes all gates.
4. Deploy using `make build` and run the workflow container.

## Troubleshooting

- **Failure during ingest**: Inspect logs for network issues with the GitHub API.
- **Analysis issues**: Verify repository name and token permissions.
- **Rollback**: Execute `python -m src.rollback` to revert actions.

## Escalation

Contact the DevOps team on call if stability cannot be confirmed after one retry.

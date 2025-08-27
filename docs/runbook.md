# Secure Repo Scorecard Remediation Runbook

## Overview

This runbook guides operators through running and troubleshooting the automated remediation workflow that leverages StepSecurity's `secure-repo` to fix OpenSSF Scorecard vulnerabilities.

## Normal Operation

1. Ensure `SECURE_REPO_TOKEN` is set in the environment.
2. Execute `make install` to install dependencies.
3. Run `make test` to verify the workflow passes all gates.
4. Deploy using `make build` and run the workflow container.

## Troubleshooting

- **Failure during scan**: Inspect logs for `scan_scorecard` step.
- **Remediation issues**: Verify network access to StepSecurity and GitHub APIs.
- **Rollback**: Execute `python -m src.rollback` to revert applied patches.

## Escalation

Contact the DevSecOps team on call if remediation cannot be completed after one retry.

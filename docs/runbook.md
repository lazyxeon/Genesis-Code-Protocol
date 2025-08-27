# Matrix CI Repair Runbook

## Overview
This runbook guides operators running the `matrix-ci-repair` workflow.

## Normal Operation
1. Trigger the workflow via GitHub push or manual dispatch.
2. Monitor job progress in GitHub Actions.
3. Review the `test_report` artifact for failures.

## Troubleshooting
- **Setup failures**: ensure required Python versions are installed on the runner.
- **Lint failures**: run `make test` locally to reproduce and fix.
- **Test failures**: inspect the report and resolve failing cases.
- **Rollback**: revert the offending commit or disable the workflow file.

## Escalation
Escalate to the DevInfra team if failures persist after two attempts or block a release.

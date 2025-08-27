# CI Workflow Diagnoser Runbook

## Overview

This runbook describes how to operate the **ci-workflow-diagnoser** workflow.

## Normal Operation

1. Run the ingest step using the provided Makefile target.
2. Review generated artifacts in the `dist/` directory.

## Failure Recovery

1. Inspect logs for error messages.
2. Re-run the workflow with increased logging if necessary.
3. Use the rollback procedure to restore previous artifacts.

# Matrix CI Runbook

1. Trigger: push to GitHub.
2. GitHub Actions runs `matrix-ci.yml` workflow.
3. Investigate failures by inspecting logs and artifacts.
4. Rollback: revert commit or disable failing job.

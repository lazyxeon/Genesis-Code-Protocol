from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict

from . import automerge, errors, rollback, utils


def run() -> str:
    """Execute Dependabot auto-merge workflow and return report path."""
    report_path = Path(os.getenv("WF_REPORT_PATH", "automerge-report.json"))
    pr_number = int(os.getenv("PR_NUMBER", "0"))
    repo = os.getenv("REPO", "")
    token = os.getenv("GITHUB_TOKEN")
    try:
        if os.getenv("WF_FAIL_STEP") == "automerge":
            raise errors.TerminalError("forced failure at automerge")
        result: Dict[str, str | int] = automerge.enable_automerge(
            pr_number, repo, token
        )
        utils.atomic_write(report_path, json.dumps(result))
        return str(report_path)
    except (errors.RetryableError, errors.TerminalError) as exc:
        rollback.perform(str(exc))
        raise


if __name__ == "__main__":
    run()

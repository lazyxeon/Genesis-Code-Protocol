from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict

from . import codacy, errors, fortify, rollback, utils


def run() -> str:
    """Execute security scans and return path to report."""
    report_path = Path(os.getenv("WF_REPORT_PATH", "scan-report.json"))
    results: Dict[str, Dict[str, str]] = {}
    try:
        if os.getenv("WF_FAIL_STEP") == "fortify":
            raise errors.TerminalError("forced failure at fortify")
        results["fortify"] = fortify.main()

        if os.getenv("WF_FAIL_STEP") == "codacy":
            raise errors.TerminalError("forced failure at codacy")
        results["codacy"] = codacy.main()

        utils.atomic_write(report_path, json.dumps(results))
        return str(report_path)
    except (errors.RetryableError, errors.TerminalError) as exc:
        rollback.perform(str(exc))
        raise


if __name__ == "__main__":
    run()

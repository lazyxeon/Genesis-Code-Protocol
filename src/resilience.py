from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict

from opentelemetry import trace

from . import errors, rollback, utils

logger = utils.get_logger(__name__)
tracer = trace.get_tracer("gha-workflow-resilience")


@dataclass
class StepResult:
    step: str
    status: str
    detail: str | None = None


def dependency_review() -> StepResult:
    with tracer.start_as_current_span("resilience.dependency_review"):
        logger.info("dependency review check")
        if not Path("requirements.txt").exists():
            raise errors.TerminalError("requirements.txt missing")
        return StepResult("dependency_review", "success")


def generate_changelog() -> StepResult:
    with tracer.start_as_current_span("resilience.generate_changelog"):
        logger.info("verify changelog")
        if not Path("CHANGELOG.md").exists():
            raise errors.TerminalError("CHANGELOG.md missing")
        return StepResult("generate_changelog", "success")


def update_toc() -> StepResult:
    with tracer.start_as_current_span("resilience.update_toc"):
        logger.info("check TOC file")
        if not Path("Table Of Contents.md").exists():
            raise errors.TerminalError("Table Of Contents.md missing")
        return StepResult("update_toc", "success")


def update_repo_structure() -> StepResult:
    with tracer.start_as_current_span("resilience.update_repo_structure"):
        logger.info("check README structure")
        if not Path("README.md").exists():
            raise errors.TerminalError("README.md missing")
        return StepResult("update_repo_structure", "success")


def markdownlint() -> StepResult:
    with tracer.start_as_current_span("resilience.markdownlint"):
        logger.info("markdownlint placeholder")
        return StepResult("markdownlint", "success")


def release_bundle() -> StepResult:
    with tracer.start_as_current_span("resilience.release_bundle"):
        logger.info("bundle placeholder")
        return StepResult("release_bundle", "success")


def sign_release() -> StepResult:
    with tracer.start_as_current_span("resilience.sign_release"):
        logger.info("sign placeholder")
        return StepResult("sign_release", "success")


STEPS: Dict[str, Callable[[], StepResult]] = {
    "dependency_review": dependency_review,
    "generate_changelog": generate_changelog,
    "update_toc": update_toc,
    "update_repo_structure": update_repo_structure,
    "markdownlint": markdownlint,
    "release_bundle": release_bundle,
    "sign_release": sign_release,
}


def run() -> str:
    """Run all steps and write a JSON report."""
    report_path = Path(os.getenv("WF_REPORT_PATH", "ci-report.json"))
    results: Dict[str, Dict[str, str]] = {}
    try:
        for name, func in STEPS.items():
            if os.getenv("WF_FAIL_STEP") == name:
                raise errors.TerminalError(f"forced failure at {name}")
            res = func()
            results[res.step] = {"status": res.status}
        utils.atomic_write(report_path, json.dumps(results))
        return str(report_path)
    except (errors.RetryableError, errors.TerminalError) as exc:
        rollback.perform(str(exc))
        raise


if __name__ == "__main__":
    run()

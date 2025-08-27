"""End-to-end smoke test."""

import json
from pathlib import Path

from src import resilience


def test_e2e_smoke(tmp_path, monkeypatch) -> None:
    """Run the main workflow and verify a report is produced."""
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.delenv("WF_FAIL_STEP", raising=False)
    result = resilience.run()
    assert Path(result).exists()
    data = json.loads(Path(result).read_text())
    for key in (
        "dependency_review",
        "generate_changelog",
        "update_toc",
        "update_repo_structure",
        "markdownlint",
        "release_bundle",
        "sign_release",
    ):
        assert key in data

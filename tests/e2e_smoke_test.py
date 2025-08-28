"""End-to-end smoke test."""

import json
from pathlib import Path

from src import main


def test_e2e_smoke(tmp_path, monkeypatch) -> None:
    """Run the main workflow and verify a report is produced."""
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("PR_NUMBER", "123")
    monkeypatch.setenv("REPO", "octo/example")
    monkeypatch.setenv("GITHUB_TOKEN", "tok")
    monkeypatch.delenv("WF_FAIL_STEP", raising=False)
    result = main.run()
    assert Path(result).exists()
    data = json.loads(Path(result).read_text())
    assert data["status"] == "enabled"
    assert data["pr"] == 123

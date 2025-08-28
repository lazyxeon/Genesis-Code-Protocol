"""Security checks."""

import json
from pathlib import Path

from src import main


def test_no_token_in_report(tmp_path, monkeypatch) -> None:
    """Verify secrets are not written to the report."""
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("PR_NUMBER", "5")
    monkeypatch.setenv("REPO", "octo/example")
    monkeypatch.setenv("GITHUB_TOKEN", "secret")
    main.run()
    assert "secret" not in report_path.read_text()


def test_policy_enforces_fail_on_critical() -> None:
    """Ensure security policy requires failing on critical vulnerabilities."""
    data = json.loads(Path("workflow_manifest.json").read_text())
    assert data["security"]["supply_chain"]["policy"] == "fail_on_critical"

import json
from pathlib import Path

from src import main


def test_no_secret_in_logs(tmp_path, monkeypatch, capsys) -> None:
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("WF_FAIL_STEP", "false")
    monkeypatch.setenv("MY_SECRET", "topsecret")
    main.run()
    captured = capsys.readouterr().out
    assert "topsecret" not in captured


def test_policy_enforces_fail_on_critical() -> None:
    data = json.loads(Path("workflow_manifest.json").read_text())
    assert data["security"]["supply_chain"]["policy"] == "fail_on_critical"

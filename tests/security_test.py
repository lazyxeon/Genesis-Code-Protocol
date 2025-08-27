import json
<<<<<< codex/develop-and-implement-matrix-ci

from matrix_ci import pipeline


def test_logs_contain_no_secret(caplog):
    pipeline.run_all()
    for record in caplog.records:
        data = json.loads(record.getMessage())
        assert "secret" not in data["message"].lower()
=======
from pathlib import Path

from src import main


def test_no_secret_in_logs(tmp_path, monkeypatch, capsys):
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("WF_FAIL_STEP", "false")
    monkeypatch.setenv("MY_SECRET", "topsecret")
    main.run()
    captured = capsys.readouterr().out
    assert "topsecret" not in captured


def test_policy_enforces_fail_on_critical():
    data = json.loads(Path("workflow_manifest.json").read_text())
    assert data["security"]["supply_chain"]["policy"] == "fail_on_critical"
>>>>>> main

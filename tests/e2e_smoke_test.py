<<<<<< codex/develop-and-implement-matrix-ci
from matrix_ci.pipeline import run_all


def test_run_all():
    assert run_all() is True
=======
import json
from pathlib import Path

from src import main


def test_e2e_smoke(tmp_path, monkeypatch):
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("WF_FAIL_STEP", "false")
    result = main.run()
    assert Path(result).exists()
    data = json.loads(Path(result).read_text())
    assert "vulnerabilities" in data
>>>>>> main

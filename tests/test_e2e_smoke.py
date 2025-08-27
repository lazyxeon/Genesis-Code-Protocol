"""End-to-end smoke test."""

import json
import pathlib
import sys
from pathlib import Path

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src import main


def test_e2e_smoke(tmp_path, monkeypatch) -> None:
    """Run the main workflow and verify a report is produced."""
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("WF_FAIL_STEP", "false")
    result = main.run()
    assert Path(result).exists()
    data = json.loads(Path(result).read_text())
    assert "vulnerabilities" in data

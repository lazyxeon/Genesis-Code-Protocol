"""Rollback behavior on failure."""

import pathlib
import sys
from pathlib import Path

import pytest

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src import main, rollback


def test_rollback_file_written(tmp_path, monkeypatch) -> None:
    """Ensure rollback creates a log file when steps fail."""
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("WF_FAIL_STEP", "true")
    with pytest.raises(Exception):
        main.run()
    assert Path("rollback.log").exists()
    Path("rollback.log").unlink()


def test_rollback_called(caplog) -> None:
    """Verify rollback handler emits log message."""
    caplog.set_level("INFO")
    try:
        rollback.apply()
        raise rollback.RemediationError("fail")
    except rollback.RemediationError:
        rollback.rollback()
    assert any("rolling back" in m for m in caplog.text.splitlines())

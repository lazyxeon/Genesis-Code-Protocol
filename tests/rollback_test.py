"""Rollback behavior on failure."""

from pathlib import Path

import pytest

from src import errors, main, rollback  # Added import for errors


def test_rollback_file_written(tmp_path, monkeypatch) -> None:
    """Ensure rollback creates a log file when steps fail."""
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("WF_FAIL_STEP", "automerge")
    with pytest.raises((RuntimeError, ValueError, errors.TerminalError)):  # Added errors.TerminalError
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

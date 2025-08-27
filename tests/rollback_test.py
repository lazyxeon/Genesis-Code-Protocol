<<<<<< codex/develop-and-implement-matrix-ci
from matrix_ci.pipeline import run_with_failure


def failing_step():
    raise RuntimeError("boom")


def test_rollback_triggered():
    state = run_with_failure(failing_step)
    assert "setup" in state.executed_steps
=======
from pathlib import Path

import pytest

from src import main


def test_rollback_file_written(tmp_path, monkeypatch):
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("WF_FAIL_STEP", "true")
    with pytest.raises(Exception):
        main.run()
    assert Path("rollback.log").exists()
    Path("rollback.log").unlink()
>>>>>> main

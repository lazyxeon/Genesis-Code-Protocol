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

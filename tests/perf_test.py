import time
<<<<<< codex/develop-and-implement-matrix-ci

from matrix_ci.pipeline import run_all


def test_run_all_performance():
    start = time.time()
    run_all()
    duration = time.time() - start
    assert duration < 1
=======
from pathlib import Path

from src import main


def test_perf_under_limit(tmp_path, monkeypatch):
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("WF_FAIL_STEP", "false")
    start = time.time()
    main.run()
    duration_ms = (time.time() - start) * 1000
    assert duration_ms < 1000
>>>>>> main

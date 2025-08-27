import time

from src import main


def test_perf_under_limit(tmp_path, monkeypatch) -> None:
    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("WF_FAIL_STEP", "false")
    start = time.time()
    main.run()
    duration_ms = (time.time() - start) * 1000
    assert duration_ms < 1000

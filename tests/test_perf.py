import time

from matrix_ci.pipeline import EnvConfig, run_all


def test_run_all_under_slo():
    config = EnvConfig(python_versions=["3.11"])
    start = time.time()
    run_all(config)
    duration_ms = (time.time() - start) * 1000
    assert duration_ms < 1200

import time

from matrix_ci.pipeline import run_all


def test_run_all_performance():
    start = time.time()
    run_all()
    duration = time.time() - start
    assert duration < 1

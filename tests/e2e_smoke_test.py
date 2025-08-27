from matrix_ci.pipeline import run_all


def test_run_all():
    assert run_all() is True

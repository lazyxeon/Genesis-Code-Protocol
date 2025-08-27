from matrix_ci.pipeline import run_with_failure


def failing_step():
    raise RuntimeError("boom")


def test_rollback_triggered():
    state = run_with_failure(failing_step)
    assert "setup" in state.executed_steps

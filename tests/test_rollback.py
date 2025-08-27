from matrix_ci.pipeline import EnvConfig, run_with_failure


def failing_step(config):
    raise RuntimeError("boom")


def test_rollback_invoked():
    config = EnvConfig(python_versions=["3.11"])
    state = run_with_failure(failing_step, config)
    assert state.executed_steps == ["setup"]

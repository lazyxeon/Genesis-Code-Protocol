from matrix_ci.pipeline import EnvConfig, run_all

def test_run_all():
    config = EnvConfig(python_versions=['3.11'])
    assert run_all(config)

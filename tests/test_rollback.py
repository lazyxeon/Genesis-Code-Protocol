from src import rollback


def test_rollback_called(caplog) -> None:
    caplog.set_level("INFO")
    try:
        rollback.apply()
        raise rollback.RemediationError("fail")
    except rollback.RemediationError:
        rollback.rollback()
    assert any("rolling back" in m for m in caplog.text.splitlines())

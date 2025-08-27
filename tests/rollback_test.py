"""Ensure rollback path executes."""
from src import rollback

def test_rollback() -> None:
    assert rollback.main("build") == "rollback-complete"

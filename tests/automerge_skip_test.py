"""Tests for automerge skip behavior."""

from src import automerge


def test_automerge_skips_without_token(caplog):
    caplog.set_level("INFO")
    result = automerge.enable_automerge(1, "octo/example", token=None)
    assert result == {"status": "skipped"}
    assert "automerge skipped" in caplog.text

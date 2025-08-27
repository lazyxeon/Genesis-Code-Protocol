"""Tests for scan skip behavior."""

from src import codacy, fortify


def test_codacy_skips_without_token(caplog):
    caplog.set_level("INFO")
    result = codacy.main()
    assert result == {"status": "skipped"}
    assert "codacy skipped" in caplog.text


def test_fortify_skips_without_env(caplog):
    caplog.set_level("INFO")
    result = fortify.main()
    assert result == {"status": "skipped"}
    assert "fortify skipped" in caplog.text

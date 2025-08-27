"""Tests for scan skip behavior."""

# isort: skip_file

from src import codacy, fortify
from src import ethicalcheck


def test_codacy_skips_without_token(caplog):
    caplog.set_level("INFO")
    result = codacy.main()
    assert result == {"status": "skipped"}
    assert "codacy skipped" in caplog.text


def test_ethicalcheck_skips_without_env(monkeypatch, caplog):
    """EthicalCheck should skip if required environment variables are missing."""
    caplog.set_level("INFO")
    monkeypatch.delenv("ETHICALCHECK_OAS_URL", raising=False)
    monkeypatch.delenv("ETHICALCHECK_EMAIL", raising=False)
    result = ethicalcheck.main()
    assert result == {"status": "skipped"}
    assert "ethicalcheck skipped" in caplog.text


def test_fortify_skips_without_env(caplog):
    caplog.set_level("INFO")
    result = fortify.main()
    assert result == {"status": "skipped"}
    assert "fortify skipped" in caplog.text

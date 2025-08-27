"""Contract interface checks."""

from pathlib import Path


def test_contract_mentions_versioning() -> None:
    """Ensure the contract documents semantic versioning and request IDs."""
    text = Path("integration_contract.md").read_text()
    assert "Semantic versioning" in text
    assert "X-Request-ID" in text


def test_contract_mentions_authentication() -> None:
    """Verify authentication section is present."""
    content = Path("integration_contract.md").read_text()
    assert "Authentication" in content


def test_contract_sections_present() -> None:
    """Check required sections exist in the contract."""
    text = Path("integration_contract.md").read_text()
    for section in ["Interfaces", "Authentication", "Idempotency", "Versioning"]:
        assert f"## {section}" in text


def test_contract_mentions_cli_and_http() -> None:
    """Ensure CLI and HTTP integration surfaces are documented."""
    text = Path("integration_contract.md").read_text()
    assert "CLI" in text and "HTTP" in text

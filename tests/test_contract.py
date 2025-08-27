from pathlib import Path


def test_contract_mentions_authentication() -> None:
    content = Path("integration_contract.md").read_text()
    assert "Authentication" in content

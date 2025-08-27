from pathlib import Path


def test_contract_mentions_cli_and_http():
    text = Path("integration_contract.md").read_text()
    assert "CLI" in text and "HTTP" in text

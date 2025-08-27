from pathlib import Path

def test_contract_mentions_authentication():
    content = Path("integration_contract.md").read_text()
    assert "Authentication" in content

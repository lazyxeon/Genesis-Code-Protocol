from pathlib import Path


<<<<<< codex/develop-and-implement-matrix-ci
def test_contract_mentions_cli_and_http():
    text = Path("integration_contract.md").read_text()
    assert "CLI" in text and "HTTP" in text
=======
def test_integration_contract_sections():
    text = Path("integration_contract.md").read_text()
    for section in ["Interfaces", "Authentication", "Idempotency", "Versioning"]:
        assert f"## {section}" in text
>>>>>> main

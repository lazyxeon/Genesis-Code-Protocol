from pathlib import Path


def test_integration_contract_sections() -> None:
    text = Path("integration_contract.md").read_text()
    for section in ["Interfaces", "Authentication", "Idempotency", "Versioning"]:
        assert f"## {section}" in text

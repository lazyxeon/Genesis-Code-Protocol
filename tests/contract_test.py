"""Check integration contract content."""
from pathlib import Path

def test_contract_has_sections() -> None:
    text = Path("integration_contract.md").read_text()
    for section in ["Interfaces", "Authentication", "Versioning"]:
        assert section in text

from pathlib import Path


def test_integration_contract_sections():
    text = Path("integration_contract.md").read_text()
    for section in [
        "Interfaces",
        "Authentication",
        "Rate Limits",
        "Error Shapes",
        "Idempotency",
        "Versioning",
        "Compatibility Tests",
    ]:
        assert section in text

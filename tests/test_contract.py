<<<<<< codex/analyze-failing-github-workflows
"""Contract interface checks."""
from pathlib import Path


def test_contract_mentions_versioning() -> None:
    text = Path("integration_contract.md").read_text()
    assert "Semantic versioning" in text
    assert "X-Request-ID" in text
=======
from pathlib import Path

def test_contract_mentions_authentication():
    content = Path("integration_contract.md").read_text()
    assert "Authentication" in content
>>>>>> main

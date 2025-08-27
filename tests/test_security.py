"""Security checks."""

import io
import json
import logging
import pathlib
import sys
from pathlib import Path

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src.utils import get_logger


def test_no_secret_in_logs() -> None:
    """Verify logs do not leak secrets."""
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger = get_logger("test")
    logger.handlers = [handler]
    logger.info("hello")
    assert "SECURE_REPO_TOKEN" not in stream.getvalue()


def test_policy_enforces_fail_on_critical() -> None:
    """Ensure security policy requires failing on critical vulnerabilities."""
    data = json.loads(Path("workflow_manifest.json").read_text())
    assert data["security"]["supply_chain"]["policy"] == "fail_on_critical"

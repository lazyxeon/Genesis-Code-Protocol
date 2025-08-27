import io
import logging

from src.utils import get_logger


def test_no_secret_in_logs(monkeypatch) -> None:
    stream = io.StringIO()
    handler = logging.StreamHandler(stream)
    logger = get_logger("test")
    logger.handlers = [handler]
    logger.info("hello")
    assert "SECURE_REPO_TOKEN" not in stream.getvalue()

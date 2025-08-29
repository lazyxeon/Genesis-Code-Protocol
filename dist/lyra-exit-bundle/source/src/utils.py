import json
import logging
import os
from pathlib import Path
from typing import Any


def atomic_write(path: Path, data: str) -> None:
    """Write ``data`` to ``path`` atomically."""
    tmp_path = Path(f"{path}.tmp")
    tmp_path.write_text(data)
    os.replace(tmp_path, path)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(_JsonFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


class _JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_entry: dict[str, Any] = {
            "level": record.levelname,
            "message": record.getMessage(),
            "name": record.name,
        }
        return json.dumps(log_entry)

<<<<<< codex/analyze-failing-github-workflows
"""Utility helpers for the workflow."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any


def atomic_write(path: Path, data: str) -> None:
    """Write ``data`` to ``path`` atomically.

    A temporary file is written first and then renamed, ensuring rollback on failure.
    """
    tmp_path = Path(f"{path}.tmp")
    tmp_path.write_text(data)
    os.replace(tmp_path, path)

=======
import json
import logging
from typing import Any

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
>>>>>> main

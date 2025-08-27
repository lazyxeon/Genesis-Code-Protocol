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


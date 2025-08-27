"""Test configuration."""

import sys
from pathlib import Path

# Ensure the project's ``src`` directory is on ``sys.path`` so that test modules
# can import the package without installing it. This mirrors the layout used in
# development and keeps tests lightweight.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))


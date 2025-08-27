import sys
from pathlib import Path

# Add Scripts directory to path for import
sys.path.append(str(Path(__file__).resolve().parents[1] / "Scripts"))

from fix_md_spacing import normalize_spacing


def test_collapse_leading_blank_lines():
    lines = ["\n", "\n", "# Heading\n"]
    assert normalize_spacing(lines) == ["\n", "# Heading\n"]

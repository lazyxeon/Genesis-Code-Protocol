import sys
from pathlib import Path

# Add Scripts directory to path for import
sys.path.append(str(Path(__file__).resolve().parents[1] / "Scripts"))

from fix_md_spacing import normalize_spacing


def test_code_fences_preserved():
    lines = [
        "Before\n",
        "```\n",
        "code\n",
        "```\n",
        "After\n",
    ]
    assert normalize_spacing(lines) == lines


def test_single_level_list_spacing():
    lines = [
        "Intro\n",
        "- item1\n",
        "- item2\n",
        "Outro\n",
    ]
    expected = [
        "Intro\n",
        "\n",
        "- item1\n",
        "- item2\n",
        "\n",
        "Outro\n",
    ]
    assert normalize_spacing(lines) == expected


def test_multi_level_list_spacing():
    lines = [
        "Intro\n",
        "- item1\n",
        "  - subitem1\n",
        "- item2\n",
        "Conclusion\n",
    ]
    expected = [
        "Intro\n",
        "\n",
        "- item1\n",
        "  - subitem1\n",
        "- item2\n",
        "\n",
        "Conclusion\n",
    ]
    assert normalize_spacing(lines) == expected


def test_collapse_consecutive_blank_lines():
    lines = [
        "Line1\n",
        "\n",
        "\n",
        "Line2\n",
        "\n",
        "\n",
        "Line3\n",
    ]
    expected = [
        "Line1\n",
        "\n",
        "Line2\n",
        "\n",
        "Line3\n",
    ]
    assert normalize_spacing(lines) == expected

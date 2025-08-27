"""Tests for the ``normalize_spacing`` utility."""

import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)  # pylint: disable=wrong-import-position
from scripts.fix_md_spacing import normalize_spacing  # noqa: E402


def test_code_fences_preserved() -> None:
    """Ensure code fences are not altered."""
    lines = [
        "Before\n",
        "```\n",
        "code\n",
        "```\n",
        "After\n",
    ]
    assert normalize_spacing(lines) == lines


def test_single_level_list_spacing() -> None:
    """Insert blank lines around single-level lists."""
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


def test_multi_level_list_spacing() -> None:
    """Insert blank lines around nested lists."""
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


def test_collapse_consecutive_blank_lines() -> None:
    """Collapse runs of blank lines into a single line."""
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

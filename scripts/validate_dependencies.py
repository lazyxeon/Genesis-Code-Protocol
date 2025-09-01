#!/usr/bin/env python3
"""Validate dependency-related files in the repository.

The script performs lightweight checks on common dependency descriptors such
as ``requirements.txt`` files, ``setup.py``, ``setup.cfg``, ``pyproject.toml``
and selected GitHub configuration files. The goal is to surface obvious issues
before they reach CI.

Usage:
    python scripts/validate_dependencies.py
"""

from __future__ import annotations

import glob
import os
import sys
from configparser import ConfigParser


def validate_requirements_file(filepath: str) -> bool:
    """Validate the format and content of a requirements file."""
    issues: list[str] = []
    warnings: list[str] = []

    try:
        with open(filepath, encoding="utf-8") as f:
            lines = f.readlines()

        dependencies: list[str] = []
        for line_num, line in enumerate(lines, 1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            dependencies.append(line)

            if not any(op in line for op in ["==", ">=", "<=", "~=", "!="]):
                if not line.startswith("-"):
                    warnings.append(
                        f"Line {line_num}: Unpinned dependency '{line}'"
                    )

            if ".." in line and not line.startswith("-r"):
                issues.append(
                    f"Line {line_num}: Suspicious path traversal pattern"
                )

            if line.startswith("http://"):
                warnings.append(f"Line {line_num}: Insecure HTTP URL")

        print(f"✓ {filepath}: {len(dependencies)} dependencies")

        if warnings:
            print(f"  ⚠ {len(warnings)} warnings:")
            for warning in warnings[:5]:
                print(f"    {warning}")

        if issues:
            print(f"  ✗ {len(issues)} issues:")
            for issue in issues:
                print(f"    {issue}")
            return False

    except Exception as exc:  # pragma: no cover - defensive
        print(f"✗ {filepath}: Error reading file - {exc}")
        return False

    return True


def validate_setup_py(filepath: str) -> bool:
    """Validate ``setup.py`` by compiling it."""
    try:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        compile(content, filepath, "exec")
        print(f"✓ {filepath}: Syntax is valid")
        return True
    except SyntaxError as exc:
        print(f"✗ {filepath}: Syntax error - {exc}")
        return False
    except Exception as exc:  # pragma: no cover - defensive
        print(f"✗ {filepath}: Error reading file - {exc}")
        return False


def validate_yaml_file(filepath: str) -> bool:
    """Validate YAML syntax using PyYAML if available."""
    try:
        import yaml

        with open(filepath, encoding="utf-8") as f:
            yaml.safe_load(f)
        print(f"✓ {filepath}: YAML syntax is valid")
        return True
    except ImportError:
        print(f"⚠ {filepath}: PyYAML not available, skipping validation")
        return True
    except Exception as exc:
        print(f"✗ {filepath}: YAML error - {exc}")
        return False


def validate_toml_file(filepath: str) -> bool:
    """Validate TOML syntax using ``tomllib`` or ``tomli``."""
    try:
        try:  # Python 3.11+
            import tomllib as toml
        except ModuleNotFoundError:  # pragma: no cover - fallback
            import tomli as toml  # type: ignore

        with open(filepath, "rb") as f:
            toml.load(f)
        print(f"✓ {filepath}: TOML syntax is valid")
        return True
    except ImportError:
        print(f"⚠ {filepath}: tomllib/tomli not available, skipping validation")
        return True
    except Exception as exc:
        print(f"✗ {filepath}: TOML error - {exc}")
        return False


def validate_cfg_file(filepath: str) -> bool:
    """Validate INI-style configuration files such as ``setup.cfg``."""
    parser = ConfigParser()
    try:
        with open(filepath, encoding="utf-8") as f:
            parser.read_file(f)
        print(f"✓ {filepath}: Config syntax is valid")
        return True
    except Exception as exc:
        print(f"✗ {filepath}: Config error - {exc}")
        return False


def find_dependency_files() -> dict[str, list[str]]:
    """Locate dependency-related files in the repository."""
    files: dict[str, list[str]] = {"requirements": [], "setup": [], "config": []}

    for pattern in ["requirements*.txt", "*requirements.txt"]:
        files["requirements"].extend(glob.glob(pattern, recursive=True))
        files["requirements"].extend(glob.glob(f"**/{pattern}", recursive=True))

    for pattern in ["setup.py", "pyproject.toml", "setup.cfg"]:
        files["setup"].extend(glob.glob(pattern))
        files["setup"].extend(glob.glob(f"**/{pattern}", recursive=True))

    for pattern in [
        ".github/dependency-review-config.yml",
        ".github/workflows/dependency-review.yml",
    ]:
        if os.path.exists(pattern):
            files["config"].append(pattern)

    for category in files:
        files[category] = list({f for f in files[category] if os.path.isfile(f)})

    return files


def main() -> int:
    """Entry point for the validator."""
    print("🔍 Dependency Validation Script")
    print("=" * 40)

    files = find_dependency_files()
    total_files = sum(len(v) for v in files.values())
    if total_files == 0:
        print("⚠ No dependency files found!")
        return 0

    print(f"Found {total_files} dependency-related files\n")

    all_valid = True

    if files["requirements"]:
        print(f"📋 Requirements Files ({len(files['requirements'])}):")
        for path in files["requirements"]:
            if not validate_requirements_file(path):
                all_valid = False
        print()

    if files["setup"]:
        print(f"⚙️ Setup Files ({len(files['setup'])}):")
        for path in files["setup"]:
            if path.endswith(".py"):
                if not validate_setup_py(path):
                    all_valid = False
            elif path.endswith(".toml"):
                if not validate_toml_file(path):
                    all_valid = False
            elif path.endswith(".cfg"):
                if not validate_cfg_file(path):
                    all_valid = False
            elif path.endswith((".yml", ".yaml")):
                if not validate_yaml_file(path):
                    all_valid = False
            else:
                print(f"⚠ {path}: Unknown file type, skipping")
        print()

    if files["config"]:
        print(f"🔧 Configuration Files ({len(files['config'])}):")
        for path in files["config"]:
            if not validate_yaml_file(path):
                all_valid = False
        print()

    if all_valid:
        print("✅ All dependency files are valid!")
        return 0

    print("❌ Some dependency files have issues that need attention.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
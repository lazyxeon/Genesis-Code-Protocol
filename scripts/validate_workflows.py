#!/usr/bin/env python3
"""Validation script to check workflow dependencies and core functionality."""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_SCRIPTS = [
    "scripts/generate_repo_toc.py",
    "scripts/update_repo_structure.py",
    "scripts/fix_md_spacing.py",
    "scripts/generate_changelog.py",
]
REQUIRED_CONFIGS = [
    ".markdownlint.yml",
    ".pre-commit-config.yaml",
]
REQUIRED_WORKFLOW_FILES = [
    ".github/workflows/update-toc-file.yml",
    ".github/workflows/update-repo-structure.yml",
    ".github/workflows/release-sign.yml",
    ".github/workflows/release-bundle.yml",
    ".github/workflows/pre-commit.yml",
    ".github/workflows/markdownlint.yml",
    ".github/workflows/generate-changelog.yml",
    ".github/workflows/sbom.yml",
    ".github/workflows/validate-workflows.yml",
]


def check_file_exists(filepath: str) -> bool:
    """Check if a file exists and is readable."""
    path = ROOT / filepath
    return path.exists() and path.is_file()


def validate_python_syntax(filepath: str) -> bool:
    """Validate Python script syntax."""
    try:
        with open(ROOT / filepath) as f:
            compile(f.read(), filepath, "exec")
        return True
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return False
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False


def main() -> int:
    """Main validation function."""
    print("Validating workflow dependencies...")

    success = True

    # Check required scripts exist
    print("\nChecking required scripts:")
    for script in REQUIRED_SCRIPTS:
        if check_file_exists(script):
            print(f"✓ {script}")
            if not validate_python_syntax(script):
                success = False
        else:
            print(f"✗ {script} - missing")
            success = False

    # Check required config files
    print("\nChecking required config files:")
    for config in REQUIRED_CONFIGS:
        if check_file_exists(config):
            print(f"✓ {config}")
        else:
            print(f"✗ {config} - missing")
            success = False

    # Check required workflow files
    print("\nChecking workflow files:")
    for workflow in REQUIRED_WORKFLOW_FILES:
        if check_file_exists(workflow):
            print(f"✓ {workflow}")
        else:
            print(f"✗ {workflow} - missing")
            success = False

    # Test core functionality
    print("\nTesting core scripts...")

    try:
        # Test TOC generation
        os.chdir(ROOT)
        import subprocess

        result = subprocess.run(
            [sys.executable, "scripts/generate_repo_toc.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            print("✓ TOC generation script works")
        else:
            print(f"✗ TOC generation failed: {result.stderr}")
            success = False
    except Exception as e:
        print(f"✗ TOC generation test failed: {e}")
        success = False

    try:
        # Test repo structure update
        result = subprocess.run(
            [sys.executable, "scripts/update_repo_structure.py"],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            print("✓ Repo structure script works")
        else:
            print(f"✗ Repo structure update failed: {result.stderr}")
            success = False
    except Exception as e:
        print(f"✗ Repo structure test failed: {e}")
        success = False

    if success:
        print("\n✓ All workflow validations passed!")
        return 0
    else:
        print("\n✗ Some validations failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())

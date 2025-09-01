#!/usr/bin/env python3
"""
Dependency Validation Script

This script validates dependency files locally before committing, 
helping to catch issues before they trigger workflow failures.

Usage:
    python scripts/validate_dependencies.py
    
Requirements:
    - Python 3.6+
    - PyYAML (for configuration validation)
"""

import glob
import os
import sys


def validate_requirements_file(filepath):
    """Validate a requirements.txt file format and content."""
    issues = []
    warnings = []

    try:
        with open(filepath, encoding='utf-8') as f:
            lines = f.readlines()

        dependencies = []
        for line_num, line in enumerate(lines, 1):
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue

            dependencies.append(line)

            # Check for common issues
            if not any(op in line for op in ['==', '>=', '<=', '~=', '!=']):
                if not line.startswith('-'):  # Skip flags like -r, -e
                    warnings.append(f"Line {line_num}: Unpinned dependency '{line}'")

            # Check for problematic patterns
            if '..' in line and not line.startswith('-r'):
                issues.append(f"Line {line_num}: Suspicious path traversal pattern")

            if line.startswith('http://'):
                warnings.append(f"Line {line_num}: Insecure HTTP URL")

        print(f"✓ {filepath}: {len(dependencies)} dependencies")

        if warnings:
            print(f"  ⚠ {len(warnings)} warnings:")
            for warning in warnings[:5]:  # Show first 5
                print(f"    {warning}")

        if issues:
            print(f"  ✗ {len(issues)} issues:")
            for issue in issues:
                print(f"    {issue}")
            return False

    except Exception as e:
        print(f"✗ {filepath}: Error reading file - {e}")
        return False

    return True


def validate_setup_py(filepath):
    """Validate setup.py file syntax."""
    try:
        # Basic syntax check
        with open(filepath, encoding='utf-8') as f:
            content = f.read()

        # Compile to check syntax
        compile(content, filepath, 'exec')
        print(f"✓ {filepath}: Syntax is valid")
        return True

    except SyntaxError as e:
        print(f"✗ {filepath}: Syntax error - {e}")
        return False
    except Exception as e:
        print(f"✗ {filepath}: Error reading file - {e}")
        return False


def validate_yaml_file(filepath):
    """Validate YAML file syntax."""
    try:
        import yaml
        with open(filepath, encoding='utf-8') as f:
            yaml.safe_load(f)
        print(f"✓ {filepath}: YAML syntax is valid")
        return True
    except ImportError:
        print(f"⚠ {filepath}: PyYAML not available, skipping validation")
        return True
    except Exception as e:
        print(f"✗ {filepath}: YAML error - {e}")
        return False


def find_dependency_files():
    """Find all dependency files in the repository."""
    files = {
        'requirements': [],
        'setup': [],
        'config': []
    }

    # Find requirements files
    for pattern in ['requirements*.txt', '*requirements.txt']:
        files['requirements'].extend(glob.glob(pattern, recursive=True))
        files['requirements'].extend(glob.glob(f'**/{pattern}', recursive=True))

    # Find setup files
    for pattern in ['setup.py', 'pyproject.toml', 'setup.cfg']:
        files['setup'].extend(glob.glob(pattern))
        files['setup'].extend(glob.glob(f'**/{pattern}', recursive=True))

    # Find config files
    for pattern in ['.github/dependency-review-config.yml', '.github/workflows/dependency-review.yml']:
        if os.path.exists(pattern):
            files['config'].append(pattern)

    # Remove duplicates and non-existent files
    for category in files:
        files[category] = list(set(f for f in files[category] if os.path.isfile(f)))

    return files


def main():
    """Main validation function."""
    print("🔍 Dependency Validation Script")
    print("=" * 40)

    # Find all dependency files
    files = find_dependency_files()

    total_files = sum(len(file_list) for file_list in files.values())
    if total_files == 0:
        print("⚠ No dependency files found!")
        return 0

    print(f"Found {total_files} dependency-related files")
    print()

    all_valid = True

    # Validate requirements files
    if files['requirements']:
        print(f"📋 Requirements Files ({len(files['requirements'])}):")
        for filepath in files['requirements']:
            if not validate_requirements_file(filepath):
                all_valid = False
        print()

    # Validate setup files
    if files['setup']:
        print(f"⚙️ Setup Files ({len(files['setup'])}):")
        for filepath in files['setup']:
            if filepath.endswith('.py'):
                if not validate_setup_py(filepath):
                    all_valid = False
            elif filepath.endswith(('.yml', '.yaml', '.toml')):
                if not validate_yaml_file(filepath):
                    all_valid = False
            else:
                print(f"⚠ {filepath}: Unknown file type, skipping")
        print()

    # Validate config files
    if files['config']:
        print(f"🔧 Configuration Files ({len(files['config'])}):")
        for filepath in files['config']:
            if not validate_yaml_file(filepath):
                all_valid = False
        print()

    # Summary
    if all_valid:
        print("✅ All dependency files are valid!")
        return 0
    else:
        print("❌ Some dependency files have issues that need attention.")
        return 1


if __name__ == '__main__':
    sys.exit(main())

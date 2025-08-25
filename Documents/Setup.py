#!/usr/bin/env python3
"""
A minimal, copy-paste ready setup.py for packaging the project.

Place this file at the repository root (or update file paths below) if you intend to
use setuptools to install the package. If you use pyproject.toml-based builds,
you can ignore this file.

This file is intentionally small and syntax-clean so automated analyzers won't fail.
"""

from pathlib import Path
from setuptools import setup, find_packages

# Adjust these values for your project
PACKAGE_NAME = "genesis_code_protocol"
VERSION = "0.0.1"
AUTHOR = "Your Name"
DESCRIPTION = "Genesis Code Protocol"
README = Path(__file__).resolve().with_name("README.md")

long_description = ""
if README.exists():
    try:
        long_description = README.read_text(encoding="utf-8")
    except Exception:
        long_description = ""

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    packages=find_packages(exclude=("tests", "docs", "Documents", "Scripts")),
    include_package_data=True,
    install_requires=[
        # Add runtime dependencies here, example:
        # "requests>=2.25.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)

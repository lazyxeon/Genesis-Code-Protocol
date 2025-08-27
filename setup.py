"""Setup configuration for the Genesis Code Protocol package."""

# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import find_packages, setup

# Read the README file for the long description.  This resolves the path
# relative to this file so that running setup from another directory still
# finds the documentation.
readme_path = Path(__file__).resolve().parents[1] / "README.md"
LONG_DESCRIPTION = ""
if readme_path.is_file():
    LONG_DESCRIPTION = readme_path.read_text(encoding="utf-8")

setup(
    name="gcp",
    version="47.0.0",
    author="LazyXeon",
    author_email="lazyxeon@example.com",
    # Avoid non-ASCII characters (e.g. non-breaking hyphens) in descriptions to
    # ensure static analysis tools like CodeQL can parse this file.  Use
    # standard ASCII hyphens instead of fancy hyphens.
    description="Genesis Code Protocol: AI-native invention framework",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/lazyxeon/Genesis-Code-Protocol",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Minimum versions are set to address known security vulnerabilities.
        "transformers>=4.53.0",
        "torch>=2.6.0",
        "scipy>=1.10.0",
        "numpy>=1.23.0",
        "pandas>=1.5.0",
        "matplotlib>=3.6.0",
        "jupyterlab>=4.2.5",
        "notebook>=7.2.2",
        "pyspark>=3.5.0",
        "sympy>=1.12.0",
        "networkx>=3.3",
        "rdkit>=2023.9.1",
        "biopython>=1.83",
        "astropy>=6.1.0",
        "pygame>=2.6.0",
    ],
    entry_points={
        "console_scripts": [
            "gcp = cli_bundle.gcp_cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)

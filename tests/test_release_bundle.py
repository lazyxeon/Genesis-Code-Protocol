#!/usr/bin/env python3
"""Test script for release bundle workflow."""

import json
import os
import subprocess
import tempfile
import zipfile
from pathlib import Path


def test_bundle_script():
    """Test the make_exit_bundle.sh script."""
    result = subprocess.run(
        ["./scripts/make_exit_bundle.sh"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"make_exit_bundle.sh failed: {result.stderr}"

    bundle_files = list(Path(".").glob("lyra-exit-bundle-*.zip"))
    assert bundle_files, "No bundle file created by make_exit_bundle.sh"

    bundle_file = bundle_files[0]

    with zipfile.ZipFile(bundle_file, "r") as zip_ref:
        contents = set(zip_ref.namelist())
        required_files = {
            "lyra-exit-bundle/rehydrate.sh",
            "lyra-exit-bundle/MANIFEST.json",
            "lyra-exit-bundle/SBOM/sbom.spdx.json",
            "lyra-exit-bundle/provenance/slsa_provenance.json",
        }
        missing = required_files - contents
        assert not missing, f"Missing required files in bundle: {missing}"

        # Validate MANIFEST.json structure
        with zip_ref.open("lyra-exit-bundle/MANIFEST.json") as f:
            manifest = json.load(f)
        for key in ["bundle_version", "created", "creator", "contents"]:
            assert key in manifest, f"Missing key in MANIFEST.json: {key}"


def test_rehydration():
    """Test that the bundle can be 'rehydrated' (basic structural checks)."""
    bundle_files = list(Path(".").glob("lyra-exit-bundle-*.zip"))
    assert bundle_files, "No bundle file found for rehydration test (run bundle script first)."
    bundle_file = bundle_files[0]

    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(bundle_file, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        bundle_dir = Path(temp_dir) / "lyra-exit-bundle"
        assert bundle_dir.exists(), "Extracted bundle directory missing."

        rehydrate_script = bundle_dir / "rehydrate.sh"
        assert rehydrate_script.exists(), "rehydrate.sh not found in bundle."

        # Ensure executable (permissions may not persist in zip)
        os.chmod(rehydrate_script, 0o755)
        assert os.access(rehydrate_script, os.X_OK), "rehydrate.sh is not executable."

        # Syntax check
        result = subprocess.run(
            ["bash", "-n", str(rehydrate_script)],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"rehydrate.sh has syntax errors: {result.stderr}"


def test_workflow_syntax():
    """Basic structural & YAML validity test for release-bundle workflow."""
    workflow_file = Path(".github/workflows/release-bundle.yml")
    assert workflow_file.exists(), "Workflow file release-bundle.yml not found."

    import yaml  # PyYAML installed via requirements

    with open(workflow_file) as f:
        content = f.read()
    data = yaml.safe_load(content)
    assert data is not None, "Workflow YAML parsed as None."

    # Some YAML parsers can interpret 'on' specially; ensure triggers exist.
    assert "name" in data, "Workflow missing 'name'."
    assert "jobs" in data, "Workflow missing 'jobs'."
    assert "on" in data, "Workflow missing 'on' trigger section."
    assert "bundle" in data["jobs"], "Workflow missing 'bundle' job."

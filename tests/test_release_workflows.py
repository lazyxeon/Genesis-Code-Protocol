"""
Test for release workflow validation
Tests the fixed sign release artifacts workflow
"""

import os
from pathlib import Path

import pytest
import yaml


def test_release_workflows_exist():
    """Test that all required release workflow files exist"""
    workflows_dir = Path(".github/workflows")

    # Check that workflow files exist
    assert (workflows_dir / "release-bundle.yml").exists()
    assert (workflows_dir / "release-sign.yml").exists()
    assert (workflows_dir / "release-complete.yml").exists()


def test_release_bundle_workflow_syntax():
    """Test that release-bundle.yml has valid syntax and structure"""
    workflow_path = Path(".github/workflows/release-bundle.yml")

    with open(workflow_path) as f:
        workflow = yaml.safe_load(f)

    # Check basic structure
    assert "name" in workflow
    assert "on" in workflow  # YAML 'on' key
    assert "jobs" in workflow

    # Check that bundle job exists and has outputs
    assert "bundle" in workflow["jobs"]
    bundle_job = workflow["jobs"]["bundle"]
    assert "outputs" in bundle_job
    assert "release-tag" in bundle_job["outputs"]
    assert "artifacts-ready" in bundle_job["outputs"]


def test_release_sign_workflow_syntax():
    """Test that release-sign.yml has valid syntax and proper job dependencies"""
    workflow_path = Path(".github/workflows/release-sign.yml")

    with open(workflow_path) as f:
        workflow = yaml.safe_load(f)

    # Check basic structure
    assert "name" in workflow
    assert "on" in workflow  # YAML 'on' key
    assert "jobs" in workflow

    # Check that wait-for-bundle job exists
    assert "wait-for-bundle" in workflow["jobs"]

    # Check that sign-release job depends on wait-for-bundle
    assert "sign-release" in workflow["jobs"]
    sign_job = workflow["jobs"]["sign-release"]
    assert "needs" in sign_job
    assert sign_job["needs"] == "wait-for-bundle"


def test_release_complete_workflow_syntax():
    """Test that release-complete.yml has valid syntax and proper job coordination"""
    workflow_path = Path(".github/workflows/release-complete.yml")

    with open(workflow_path) as f:
        workflow = yaml.safe_load(f)

    # Check basic structure
    assert "name" in workflow
    assert "on" in workflow  # YAML 'on' key
    assert "jobs" in workflow

    # Check that jobs exist in correct order
    assert "create-bundle" in workflow["jobs"]
    assert "sign-artifacts" in workflow["jobs"]

    # Check that sign-artifacts depends on create-bundle
    sign_job = workflow["jobs"]["sign-artifacts"]
    assert "needs" in sign_job
    assert sign_job["needs"] == "create-bundle"


def test_workflow_permissions():
    """Test that workflows have appropriate permissions"""
    workflow_path = Path(".github/workflows/release-complete.yml")

    with open(workflow_path) as f:
        workflow = yaml.safe_load(f)

    # Check default permissions
    assert "permissions" in workflow
    assert workflow["permissions"]["contents"] == "read"

    # Check job-specific permissions
    create_job = workflow["jobs"]["create-bundle"]
    assert "permissions" in create_job
    assert create_job["permissions"]["contents"] == "write"

    sign_job = workflow["jobs"]["sign-artifacts"]
    assert "permissions" in sign_job
    assert sign_job["permissions"]["contents"] == "write"
    assert sign_job["permissions"]["id-token"] == "write"


def test_workflow_triggers():
    """Test that workflows have correct triggers"""
    workflow_path = Path(".github/workflows/release-complete.yml")

    with open(workflow_path) as f:
        workflow = yaml.safe_load(f)

    # Check triggers (YAML 'on' key)
    assert "on" in workflow
    on_config = workflow["on"]
    assert "release" in on_config
    assert "workflow_dispatch" in on_config

    # Check release trigger types
    assert "types" in on_config["release"]
    assert "published" in on_config["release"]["types"]


def test_cosign_installation():
    """Test that cosign is properly installed in signing workflow"""
    workflow_path = Path(".github/workflows/release-complete.yml")

    with open(workflow_path) as f:
        workflow = yaml.safe_load(f)

    sign_job = workflow["jobs"]["sign-artifacts"]
    steps = sign_job["steps"]

    # Find cosign installation step
    cosign_step = None
    for step in steps:
        if step.get("name") == "Install Cosign":
            cosign_step = step
            break

    assert cosign_step is not None
    assert "uses" in cosign_step
    assert "sigstore/cosign-installer" in cosign_step["uses"]
    assert "with" in cosign_step
    assert "cosign-release" in cosign_step["with"]


def test_error_handling():
    """Test that workflows have proper error handling"""
    workflow_path = Path(".github/workflows/release-complete.yml")

    with open(workflow_path) as f:
        content = f.read()

    # Check for error handling patterns
    assert "set -euo pipefail" in content  # Bash strict mode
    assert "exit 1" in content  # Explicit error exits
    assert "max_attempts" in content  # Retry logic
    assert "verification_failed" in content  # Verification error handling


def test_exit_wizard_integration():
    """Test that the workflow includes Exit Wizard pattern integration"""
    workflow_path = Path(".github/workflows/release-complete.yml")

    with open(workflow_path) as f:
        content = f.read()

    # Check for Exit Wizard pattern elements
    assert "EXIT_WIZARD_MANIFEST.json" in content
    assert "RFC 3161" in content
    assert "transparency log" in content
    assert "Exit Wizard" in content
    assert "Genesis Code Protocol" in content


def test_timestamp_integration():
    """Test that RFC 3161 timestamp integration is included"""
    workflow_path = Path(".github/workflows/release-complete.yml")

    with open(workflow_path) as f:
        content = f.read()

    # Check for timestamp-related content
    assert "openssl ts" in content
    assert "freetsa.org" in content
    assert "timestamp" in content.lower()
    assert ".tsr" in content


def test_comprehensive_verification():
    """Test that the workflow includes comprehensive verification"""
    workflow_path = Path(".github/workflows/release-complete.yml")

    with open(workflow_path) as f:
        content = f.read()

    # Check for verification steps
    assert "verification_failed" in content
    assert "cosign verify-blob" in content
    assert "Verification successful" in content
    assert "Verification failed" in content


if __name__ == "__main__":
    # Change to repository root for testing
    repo_root = Path(__file__).parent.parent
    os.chdir(repo_root)

    # Run tests
    pytest.main([__file__, "-v"])

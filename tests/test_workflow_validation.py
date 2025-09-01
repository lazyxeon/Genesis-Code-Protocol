#!/usr/bin/env python3
"""
Comprehensive workflow validation tests
Tests that all GitHub workflows are properly configured and working
"""

from pathlib import Path

import pytest
import yaml


class TestWorkflowValidation:
    """Test suite for GitHub workflow validation"""

    @pytest.fixture
    def workflows_dir(self):
        """Return the workflows directory path"""
        return Path(".github/workflows")

    @pytest.fixture
    def workflow_files(self, workflows_dir):
        """Return list of all workflow files"""
        return list(workflows_dir.glob("*.yml"))

    def test_all_workflows_exist(self, workflows_dir):
        """Test that the workflows directory exists and contains files"""
        assert workflows_dir.exists(), "Workflows directory should exist"
        workflow_files = list(workflows_dir.glob("*.yml"))
        assert len(workflow_files) > 0, "Should have at least one workflow file"

    def test_workflow_yaml_syntax(self, workflow_files):
        """Test that all workflow files have valid YAML syntax"""
        for workflow_file in workflow_files:
            with open(workflow_file) as f:
                try:
                    yaml.safe_load(f)
                except yaml.YAMLError as e:
                    pytest.fail(f"Invalid YAML syntax in {workflow_file}: {e}")

    def test_workflow_required_fields(self, workflow_files):
        """Test that all workflows have required fields"""
        for workflow_file in workflow_files:
            with open(workflow_file) as f:
                workflow = yaml.safe_load(f)

            # Check required top-level fields
            assert "name" in workflow, f"{workflow_file} should have a 'name' field"
            assert "on" in workflow or True in workflow, (
                f"{workflow_file} should have an 'on' trigger field"
            )
            assert "jobs" in workflow, f"{workflow_file} should have 'jobs' field"

            # Check that jobs have required fields
            for job_name, job_config in workflow["jobs"].items():
                assert "runs-on" in job_config, (
                    f"Job '{job_name}' in {workflow_file} should have 'runs-on'"
                )
                assert "steps" in job_config, (
                    f"Job '{job_name}' in {workflow_file} should have 'steps'"
                )

    def test_action_versions_consistency(self, workflow_files):
        """Test that action versions are consistent across workflows"""
        action_versions = {}

        for workflow_file in workflow_files:
            with open(workflow_file) as f:
                content = f.read()
                workflow = yaml.safe_load(content)

            # Extract action versions from workflow
            for _, job_config in workflow.get("jobs", {}).items():
                for step in job_config.get("steps", []):
                    if "uses" in step:
                        action = step["uses"]
                        action_name = action.split("@")[0]
                        action_version = action.split("@")[1] if "@" in action else "latest"

                        if action_name not in action_versions:
                            action_versions[action_name] = set()
                        action_versions[action_name].add(action_version)

        # Check for consistent versions
        inconsistent_actions = []
        for action_name, versions in action_versions.items():
            if len(versions) > 1:
                inconsistent_actions.append(f"{action_name}: {versions}")

        if inconsistent_actions:
            pytest.fail(f"Inconsistent action versions found: {inconsistent_actions}")

    def test_no_duplicate_checkout_actions(self, workflow_files):
        """Test that workflows don't have unnecessary duplicate checkout actions"""
        for workflow_file in workflow_files:
            with open(workflow_file) as f:
                workflow = yaml.safe_load(f)

            for job_name, job_config in workflow.get("jobs", {}).items():
                checkout_count = 0
                for step in job_config.get("steps", []):
                    if "uses" in step and "actions/checkout@" in step["uses"]:
                        checkout_count += 1

                # Allow maximum 1 checkout per job (some legitimate cases may need 2)
                assert checkout_count <= 2, (
                    f"Job '{job_name}' in {workflow_file} has {checkout_count} checkout actions "
                    f"(max 2 recommended)"
                )

    def test_security_permissions_defined(self, workflow_files):
        """Test that workflows have proper permissions defined"""
        for workflow_file in workflow_files:
            with open(workflow_file) as f:
                workflow = yaml.safe_load(f)

            # Check if permissions are defined at workflow or job level
            has_workflow_permissions = "permissions" in workflow
            has_job_permissions = any(
                "permissions" in job_config for job_config in workflow.get("jobs", {}).values()
            )

            assert has_workflow_permissions or has_job_permissions, (
                f"{workflow_file} should define permissions at workflow or job level"
            )

    def test_critical_workflows_present(self, workflows_dir):
        """Test that critical workflows are present"""
        critical_workflows = [
            "Python-CI.yml",
            "matrix-ci.yml",
            "pre-commit.yml",
            "markdownlint.yml",
            "generate-changelog.yml",
            "update-repo-structure.yml",
            "update-toc-file.yml",
            "validate-notebooks.yml",
            "dependency-review.yml",
        ]

        existing_workflows = [f.name for f in workflows_dir.glob("*.yml")]

        for critical_workflow in critical_workflows:
            assert critical_workflow in existing_workflows, (
                f"Critical workflow {critical_workflow} is missing"
            )

    def test_workflow_scripts_exist(self):
        """Test that scripts referenced by workflows exist"""
        script_references = [
            "scripts/generate_repo_toc.py",
            "scripts/update_repo_structure.py",
            "scripts/fix_md_spacing.py",
            "scripts/generate_changelog.py",
            "scripts/make_exit_bundle.sh",
            "scripts/validate_workflows.py",
        ]

        for script_ref in script_references:
            script_path = Path(script_ref)
            assert script_path.exists(), (
                f"Script {script_ref} referenced by workflows does not exist"
            )

    def test_config_files_exist(self):
        """Test that configuration files referenced by workflows exist"""
        config_files = [
            ".markdownlint.yml",
            ".pre-commit-config.yaml",
            "requirements.txt",
            "requirements-dev.txt",
            ".github/workflows/notebook-lint-requirements.txt",
        ]

        for config_file in config_files:
            config_path = Path(config_file)
            assert config_path.exists(), (
                f"Config file {config_file} referenced by workflows does not exist"
            )

    def test_no_hardcoded_secrets(self, workflow_files):
        """Test that workflows don't contain hardcoded secrets or tokens"""
        sensitive_patterns = [
            "ghp_",  # GitHub personal access tokens
            "ghs_",  # GitHub app tokens
            "gho_",  # GitHub OAuth tokens
            "github_pat_",  # GitHub personal access tokens (new format)
            "sk-",  # OpenAI API keys
            "AKIA",  # AWS access keys
            "AIza",  # Google API keys
        ]

        for workflow_file in workflow_files:
            with open(workflow_file) as f:
                content = f.read()

            for pattern in sensitive_patterns:
                assert pattern not in content, (
                    f"Potential hardcoded secret found in {workflow_file}: pattern '{pattern}'"
                )

    def test_workflow_timeout_limits(self, workflow_files):
        """Test that workflows have reasonable timeout limits"""
        for workflow_file in workflow_files:
            with open(workflow_file) as f:
                workflow = yaml.safe_load(f)

            for job_name, job_config in workflow.get("jobs", {}).items():
                if "timeout-minutes" in job_config:
                    timeout = job_config["timeout-minutes"]
                    assert timeout <= 360, (
                        f"Job '{job_name}' in {workflow_file} has excessive timeout: {timeout} minutes "
                        f"(max 360 recommended)"
                    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

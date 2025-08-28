"""Tests for automerge skip behavior."""

import pytest
from unittest.mock import patch, Mock

from src import automerge
from src.errors import TerminalError, RetryableError


def test_automerge_skips_without_token(caplog):
    caplog.set_level("INFO")
    result = automerge.enable_automerge(1, "octo/example", token=None)
    assert result == {"status": "skipped"}
    assert "automerge skipped" in caplog.text


def test_automerge_fails_with_invalid_pr_number():
    with pytest.raises(TerminalError, match="Invalid PR number"):
        automerge.enable_automerge(0, "octo/example", "fake-token")
    
    with pytest.raises(TerminalError, match="Invalid PR number"):
        automerge.enable_automerge(-1, "octo/example", "fake-token")


def test_automerge_fails_with_invalid_repo_format():
    with pytest.raises(TerminalError, match="Invalid repo format"):
        automerge.enable_automerge(1, "invalid-repo", "fake-token")
    
    with pytest.raises(TerminalError, match="Invalid repo format"):
        automerge.enable_automerge(1, "", "fake-token")


@patch('src.automerge.requests.get')
def test_automerge_fails_with_pr_not_found(mock_get):
    mock_get.return_value.status_code = 404
    
    with pytest.raises(TerminalError, match="PR #1 not found"):
        automerge.enable_automerge(1, "octo/example", "fake-token")


@patch('src.automerge.requests.get')
def test_automerge_fails_with_unauthorized(mock_get):
    mock_get.return_value.status_code = 401
    
    with pytest.raises(TerminalError, match="GitHub token is invalid"):
        automerge.enable_automerge(1, "octo/example", "fake-token")


@patch('src.automerge.requests.get')
def test_automerge_retries_on_server_error(mock_get):
    mock_get.return_value.status_code = 500
    
    with pytest.raises(RetryableError, match="GitHub API server error"):
        automerge.enable_automerge(1, "octo/example", "fake-token")


@patch('src.automerge.requests.get')
def test_automerge_fails_with_non_dependabot_author(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "user": {"login": "human-user"},
        "state": "open",
        "mergeable": True,
        "node_id": "PR_123"
    }
    mock_get.return_value = mock_response
    
    with pytest.raises(TerminalError, match="not authored by dependabot"):
        automerge.enable_automerge(1, "octo/example", "fake-token")


@patch('src.automerge.requests.post')
@patch('src.automerge.requests.get')
def test_automerge_success(mock_get, mock_post, caplog):
    caplog.set_level("INFO")
    
    # Mock PR details response
    mock_pr_response = Mock()
    mock_pr_response.status_code = 200
    mock_pr_response.json.return_value = {
        "user": {"login": "dependabot[bot]"},
        "state": "open",
        "mergeable": True,
        "node_id": "PR_123"
    }
    mock_get.return_value = mock_pr_response
    
    # Mock GraphQL response
    mock_graphql_response = Mock()
    mock_graphql_response.status_code = 200
    mock_graphql_response.json.return_value = {
        "data": {
            "enablePullRequestAutoMerge": {
                "pullRequest": {
                    "id": "PR_123",
                    "number": 1,
                    "autoMergeRequest": {
                        "enabledAt": "2023-01-01T00:00:00Z",
                        "mergeMethod": "SQUASH"
                    }
                }
            }
        }
    }
    mock_post.return_value = mock_graphql_response
    
    result = automerge.enable_automerge(1, "octo/example", "fake-token")
    
    assert result["status"] == "enabled"
    assert result["pr"] == 1
    assert result["repo"] == "octo/example"
    assert result["merge_method"] == "squash"
    assert "automerge enabled successfully" in caplog.text

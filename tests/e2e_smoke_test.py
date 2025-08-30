"""End-to-end smoke test."""

import json
from pathlib import Path
from unittest.mock import Mock, patch

from src import main


@patch('src.automerge.requests.post')
@patch('src.automerge.requests.get')
def test_e2e_smoke(mock_get, mock_post, tmp_path, monkeypatch) -> None:
    """Run the main workflow and verify a report is produced."""
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
                    "number": 123,
                    "autoMergeRequest": {
                        "enabledAt": "2023-01-01T00:00:00Z",
                        "mergeMethod": "SQUASH"
                    }
                }
            }
        }
    }
    mock_post.return_value = mock_graphql_response

    report_path = tmp_path / "report.json"
    monkeypatch.setenv("WF_REPORT_PATH", str(report_path))
    monkeypatch.setenv("PR_NUMBER", "123")
    monkeypatch.setenv("REPO", "octo/example")
    monkeypatch.setenv("GITHUB_TOKEN", "tok")
    monkeypatch.delenv("WF_FAIL_STEP", raising=False)

    result = main.run()
    assert Path(result).exists()
    data = json.loads(Path(result).read_text())
    assert data["status"] == "enabled"
    assert data["pr"] == 123

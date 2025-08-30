"""Security checks."""

import json
from pathlib import Path
from unittest.mock import Mock, patch

from src import main


@patch('src.automerge.requests.post')
@patch('src.automerge.requests.get')
def test_no_token_in_report(mock_get, mock_post, tmp_path, monkeypatch) -> None:
    """Verify secrets are not written to the report."""
    # Mock PR details response
    mock_pr_response = Mock()
    mock_pr_response.status_code = 200
    mock_pr_response.json.return_value = {
        "user": {"login": "dependabot[bot]"},
        "state": "open",
        "mergeable": True,
        "node_id": "PR_5"
    }
    mock_get.return_value = mock_pr_response

    # Mock GraphQL response
    mock_graphql_response = Mock()
    mock_graphql_response.status_code = 200
    mock_graphql_response.json.return_value = {
        "data": {
            "enablePullRequestAutoMerge": {
                "pullRequest": {
                    "id": "PR_5",
                    "number": 5,
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
    monkeypatch.setenv("PR_NUMBER", "5")
    monkeypatch.setenv("REPO", "octo/example")
    monkeypatch.setenv("GITHUB_TOKEN", "secret")

    main.run()
    assert "secret" not in report_path.read_text()


def test_policy_enforces_fail_on_critical() -> None:
    """Ensure security policy requires failing on critical vulnerabilities."""
    data = json.loads(Path("workflow_manifest.json").read_text())
    assert data["security"]["supply_chain"]["policy"] == "fail_on_critical"

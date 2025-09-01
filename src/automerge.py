from __future__ import annotations

import os
from typing import Any

import requests

from .errors import RetryableError, TerminalError
from .utils import get_logger

logger = get_logger(__name__)


class AutoMergeError(Exception):
    """Raised when auto-merge cannot be enabled."""


def enable_automerge(pr_number: int, repo: str, token: str | None) -> dict[str, Any]:
    """Enable auto-merge for a PR.

    Returns a status dictionary; if token is missing the step is skipped.
    """
    if not token:
        logger.info("automerge skipped: missing token")
        return {"status": "skipped"}

    if not pr_number or pr_number <= 0:
        logger.error("invalid PR number", extra={"pr": pr_number})
        raise TerminalError(f"Invalid PR number: {pr_number}")

    if not repo or "/" not in repo:
        logger.error("invalid repo format", extra={"repo": repo})
        raise TerminalError(f"Invalid repo format: {repo}")

    try:
        # Parse repo owner and name
        owner, repo_name = repo.split("/", 1)

        # First verify the PR exists and is from dependabot
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        # Get PR details
        pr_url = f"https://api.github.com/repos/{owner}/{repo_name}/pulls/{pr_number}"
        pr_response = requests.get(pr_url, headers=headers, timeout=30)

        if pr_response.status_code == 404:
            logger.error("PR not found", extra={"pr": pr_number, "repo": repo})
            raise TerminalError(f"PR #{pr_number} not found in {repo}")
        elif pr_response.status_code == 401:
            logger.error("unauthorized access", extra={"pr": pr_number, "repo": repo})
            raise TerminalError("GitHub token is invalid or lacks permissions")
        elif pr_response.status_code >= 500:
            logger.warning("GitHub API server error", extra={"status": pr_response.status_code})
            raise RetryableError(f"GitHub API server error: {pr_response.status_code}")
        elif pr_response.status_code != 200:
            logger.error(
                "unexpected GitHub API response", extra={"status": pr_response.status_code}
            )
            raise TerminalError(f"Unexpected GitHub API response: {pr_response.status_code}")

        pr_data = pr_response.json()

        # Verify it's a dependabot PR
        if pr_data.get("user", {}).get("login") != "dependabot[bot]":
            logger.error(
                "PR not authored by dependabot",
                extra={"pr": pr_number, "author": pr_data.get("user", {}).get("login")},
            )
            raise TerminalError(f"PR #{pr_number} is not authored by dependabot")

        # Check if PR is mergeable
        if pr_data.get("state") != "open":
            logger.error("PR is not open", extra={"pr": pr_number, "state": pr_data.get("state")})
            raise TerminalError(f"PR #{pr_number} is not open")

        if pr_data.get("mergeable") is False:
            logger.error("PR is not mergeable", extra={"pr": pr_number})
            raise TerminalError(f"PR #{pr_number} is not mergeable")

        # Enable auto-merge using GraphQL mutation
        graphql_url = "https://api.github.com/graphql"
        mutation = """
        mutation EnableAutoMerge($pullRequestId: ID!, $mergeMethod: PullRequestMergeMethod!) {
          enablePullRequestAutoMerge(input: {
            pullRequestId: $pullRequestId,
            mergeMethod: $mergeMethod
          }) {
            pullRequest {
              id
              number
              autoMergeRequest {
                enabledAt
                mergeMethod
              }
            }
          }
        }
        """

        variables = {"pullRequestId": pr_data["node_id"], "mergeMethod": "SQUASH"}

        graphql_payload = {"query": mutation, "variables": variables}

        graphql_response = requests.post(
            graphql_url, json=graphql_payload, headers=headers, timeout=30
        )

        if graphql_response.status_code >= 500:
            logger.warning(
                "GraphQL API server error", extra={"status": graphql_response.status_code}
            )
            raise RetryableError(f"GitHub GraphQL API server error: {graphql_response.status_code}")
        elif graphql_response.status_code != 200:
            logger.error("GraphQL API error", extra={"status": graphql_response.status_code})
            raise TerminalError(f"GitHub GraphQL API error: {graphql_response.status_code}")

        graphql_data = graphql_response.json()

        if "errors" in graphql_data:
            errors = graphql_data["errors"]
            logger.error("GraphQL mutation failed", extra={"errors": errors})
            raise TerminalError(f"Failed to enable auto-merge: {errors}")

        # Check if auto-merge was successfully enabled
        auto_merge_data = graphql_data.get("data", {}).get("enablePullRequestAutoMerge", {})
        if not auto_merge_data:
            logger.error("auto-merge not enabled", extra={"pr": pr_number})
            raise TerminalError("Auto-merge was not enabled")

        logger.info(
            "automerge enabled successfully",
            extra={"pr": pr_number, "repo": repo, "merge_method": "SQUASH"},
        )

        return {
            "status": "enabled",
            "pr": pr_number,
            "repo": repo,
            "merge_method": "squash",
            "enabled_at": auto_merge_data.get("pullRequest", {})
            .get("autoMergeRequest", {})
            .get("enabledAt"),
        }

    except requests.exceptions.Timeout as err:
        logger.warning("GitHub API timeout", extra={"pr": pr_number, "repo": repo})
        raise RetryableError("GitHub API request timed out") from err
    except requests.exceptions.ConnectionError as err:
        logger.warning("GitHub API connection error", extra={"pr": pr_number, "repo": repo})
        raise RetryableError("Failed to connect to GitHub API") from err
    except requests.exceptions.RequestException as e:
        logger.error("GitHub API request failed", extra={"error": str(e)})
        raise TerminalError(f"GitHub API request failed: {e}") from e


def main() -> dict[str, Any]:
    """Entrypoint used by the workflow step."""
    pr = int(os.getenv("PR_NUMBER", "0"))
    repo = os.getenv("REPO", "")
    token = os.getenv("GITHUB_TOKEN")
    return enable_automerge(pr, repo, token)


if __name__ == "__main__":
    print(main())

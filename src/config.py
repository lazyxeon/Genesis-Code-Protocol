from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    repo: str
    token: str

    @staticmethod
    def from_env(repo: str) -> "Settings":
        token = os.environ.get("SECURE_REPO_TOKEN", "")
        if not token:
            raise RuntimeError("SECURE_REPO_TOKEN not set")
        return Settings(repo=repo, token=token)

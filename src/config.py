"""Configuration for the build pipeline stabilizer."""
from dataclasses import dataclass
import os

@dataclass(slots=True)
class Config:
    source_archive: str = os.getenv("SOURCE_ARCHIVE", "source.tar")
    registry: str = os.getenv("REGISTRY", "registry.example/repo")
    sbom_tool: str = os.getenv("SBOM_TOOL", "syft")

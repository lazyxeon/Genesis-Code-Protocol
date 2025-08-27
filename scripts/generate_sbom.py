#!/usr/bin/env python3
"""Generate a minimal SBOM listing Python package dependencies."""
from __future__ import annotations

import json
import sys
from importlib import metadata
from pathlib import Path


def main(path: str = "sbom.json") -> None:
    packages = []
    for dist in metadata.distributions():
        name = dist.metadata.get("Name") or dist.metadata.get("Summary") or dist.metadata.get("name", "")
        packages.append({"name": name, "version": dist.version})
    data = {"packages": packages}
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Wrote SBOM with {len(packages)} packages to {path}")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "sbom.json"
    main(target)

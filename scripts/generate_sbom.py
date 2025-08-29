#!/usr/bin/env python3
"""Generate a minimal SBOM listing Python package dependencies."""
from __future__ import annotations

import json
import sys
from collections.abc import Mapping
from importlib import metadata
from pathlib import Path
from typing import cast


def main(path: str = "sbom.json") -> None:
    packages = []
    for dist in metadata.distributions():
        meta = cast(Mapping[str, str], dist.metadata)
        if "Name" in meta:
            name = meta["Name"]
        elif "Summary" in meta:
            name = meta["Summary"]
        elif "name" in meta:
            name = meta["name"]
        else:
            name = ""
        packages.append({"name": name, "version": dist.version})
    data = {"packages": packages}
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(f"Wrote SBOM with {len(packages)} packages to {path}")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "sbom.json"
    main(target)

<<<<<< codex/develop-and-implement-matrix-ci
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
=======
<<<<<< codex/analyze-failing-github-workflows
"""Test configuration."""
=======
>>>>>> main
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
>>>>>> main

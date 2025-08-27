import sys, pathlib

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src import rollback

def test_rollback_called(caplog):
    caplog.set_level("INFO")
    try:
        rollback.apply()
        raise rollback.RemediationError("fail")
    except rollback.RemediationError:
        rollback.rollback()
    assert any("rolling back" in m for m in caplog.text.splitlines())

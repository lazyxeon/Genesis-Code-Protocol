import json

from matrix_ci import pipeline


def test_logs_contain_no_secret(caplog):
    pipeline.run_all()
    for record in caplog.records:
        data = json.loads(record.getMessage())
        assert "secret" not in data["message"].lower()

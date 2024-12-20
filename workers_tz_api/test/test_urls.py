from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_team():
    response = client.get("/api/v1/team/1/WorkerList")
    assert response.status_code == 200


def test_read_worker():
    response = client.get("/api/v1/worker/1")
    assert response.status_code == 200

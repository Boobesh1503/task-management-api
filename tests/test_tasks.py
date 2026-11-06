import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_task_crud():
    created = client.post("/api/v1/tasks", json={"title": "Write tests", "description": "API test"})
    assert created.status_code == 201
    task_id = created.json()["id"]

    fetched = client.get(f"/api/v1/tasks/{task_id}")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == "Write tests"

    updated = client.put(f"/api/v1/tasks/{task_id}", json={"status": "completed"})
    assert updated.status_code == 200
    assert updated.json()["status"] == "completed"

    deleted = client.delete(f"/api/v1/tasks/{task_id}")
    assert deleted.status_code == 204

    missing = client.get(f"/api/v1/tasks/{task_id}")
    assert missing.status_code == 404

def test_invalid_status_rejected():
    response = client.put("/api/v1/tasks/999999", json={"status": "done"})
    assert response.status_code == 422

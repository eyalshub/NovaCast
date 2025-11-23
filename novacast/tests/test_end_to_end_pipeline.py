import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_end_to_end_pipeline():
    # Test health endpoint
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

    # Test chatbot interaction
    response = client.post("/api/v1/chatbot", json={"message": "Hello"})
    assert response.status_code == 200
    assert "response" in response.json()

    # Test media processing
    response = client.post("/api/v1/media", json={"script": "Sample script"})
    assert response.status_code == 202
    assert "task_id" in response.json()

    # Test schedule creation
    response = client.post("/api/v1/schedules", json={"name": "Test Schedule", "cron": "0 * * * *"})
    assert response.status_code == 201
    assert "id" in response.json()

    # Test asset upload
    response = client.post("/api/v1/assets", json={"file": "test_asset.mp4"})
    assert response.status_code == 201
    assert "url" in response.json()

    # Test prompt creation
    response = client.post("/api/v1/prompts", json={"text": "Test prompt"})
    assert response.status_code == 201
    assert "id" in response.json()
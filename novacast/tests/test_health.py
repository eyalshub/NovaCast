import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_readiness_check():
    response = client.get("/api/v1/health/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}

def test_liveness_check():
    response = client.get("/api/v1/health/liveness")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}
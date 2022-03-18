from email.mime import application
import pytest
from .application import app
from fastapi.testclient import TestClient


client = TestClient(app)
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "app is running", "success": True}
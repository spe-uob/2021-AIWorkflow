from email.mime import application
import pytest
import server.routers.internal
import server.routers.tweets
from .application import app 
from fastapi.testclient import TestClient


client = TestClient(app)
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "app is running", "success": True}

def test_login():
    response = client.get("/user/login")
    assert response.status_code == 200

def test_logout():
    response = client.get("/user/logout")
    assert response.status_code == 200
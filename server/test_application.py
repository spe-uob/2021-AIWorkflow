from email.mime import application
import pytest
import server.routers.internal
import server.routers.tweets
from .routers.tweets import user_router
from .application import app 
from fastapi.testclient import TestClient


client = TestClient(app)
client1 = TestClient(user_router)
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "app is running", "success": True}

def test_login():
    response = client1.get("/login")
    assert response.status_code == 200

def test_logout():
    response = client1.get("/logout")
    assert response.status_code == 200
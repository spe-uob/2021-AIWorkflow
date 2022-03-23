from .application import app 
from .routers import tweets
from .routers.tweets import user_router
from fastapi.testclient import TestClient

app.include_router(user_router)
app.include_router(tweets.router)

client = TestClient(app)
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "app is running", "success": True}

def test_login():
    response = client.post("/user/login")
    assert response.status_code == 200

def test_logout():
    response = client.post("/user/logout")
    assert response.status_code == 200
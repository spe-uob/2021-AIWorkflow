
from application import app 
from routers.routers import user_router, tweet_router, workflow_router
from fastapi.testclient import TestClient

client = TestClient(app)
app.include_router(tweet_router)
app.include_router(user_router)
app.include_router(workflow_router)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "app is running", "success": True}

def test_tweets():
    response = client.post("/twitterapi/tweets", json = {"user_id": "string", "tweet_text": "string", "keyword": "string", "overall_tone":"string", "specified_tone":["string"], "tone_score":0})
    assert response.status_code == 200

def test_users():
    response = client.get("/user/")
    assert response.status_code == 200

def test_workflow():
    response = client.get("/workflow/")
    assert response.status_code == 200
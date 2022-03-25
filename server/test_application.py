
from server.application import app 
from server.routers import tweets
from server.routers.tweets import user_router
from fastapi.testclient import TestClient

client = TestClient(app)
app.include_router(user_router)
app.include_router(tweets.router)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "app is running", "success": True}

def test_tweets():
    response = client.post("/twitterapi/tweets", json = {"user_id": "string", "tweet_text": "string", "keyword": "string", "overall_tone":"string", "specified_tone":["string"], "tone_score":0})
    assert response.status_code == 200
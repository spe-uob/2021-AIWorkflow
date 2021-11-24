from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()


class Item(BaseModel):
    user_id: str
    tweet_text: str
    keyword: str
    tone: str
    tone_score: Optional[int] = None
    success: bool


app = FastAPI()


@app.route("/", methods = ["POST", "GET"])
def root():
    return "app is running", 200


@app.route("/twitterapi_tweets_save", methods = ["POST"])
def twitterapi_tweets_save() :
    response = {
            "data": {
      "tweet_id": "123456789",
    },
    "message": "saved tweet successfully",
    "success": True
    }

from typing import Optional, List
from pydantic import BaseModel


class TweetRequest(BaseModel):
    user_id: str
    tweet_id: int


class TweetModel(BaseModel):
    text: str
    url: str


class TweetResponse(BaseModel):
    tweets: List[TweetModel]


class SearchTweetsResponse(BaseModel):
    data: TweetResponse
    message: str
    success: bool


class SaveTweetsRequest(BaseModel):
    user_id: str
    tweet_text: str
    keyword: str
    overall_tone: str
    specified_tone: Optional[List[str]]
    tone_score: Optional[int] = None


class SaveTweetsResponse(BaseModel):
    data: Optional[dict] = None
    message: str
    success: bool

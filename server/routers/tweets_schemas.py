from typing import Optional, List
from pydantic import BaseModel

class TweetModel(BaseModel):
    text: str
    url: str


class TweetResponse(BaseModel):
    tweets: List[TweetModel]


class SearchTweetsRequest(BaseModel):
    user_id: str
    key_word: str
    time_start: Optional[str] = None
    time_end: Optional[str] = None
    tones: List[str]


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



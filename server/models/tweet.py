from typing import Optional, List
from pydantic import BaseModel, Field, constr, ValidationError
from datetime import datetime
import tone as tone


class TweetSchema(BaseModel):
    user_id: str = Field(None)
    content: str = Field(...)
    primary_tone: tone.PrimaryTone = Field(...)
    secondary_tones: list = Field(...)
    time: datetime = Field(None)

    class Config:
        schema_extra = {
            "example": {
                "user_id": "16f78a7d6317f102bbd95fc9a4f3ff2e3249287690b8bdad6b7810f82b34ace3",
                "content": "I dislike IBM",
                "primary_tone": tone.PrimaryTone.NEGATIVE,
                "secondary_tones": [],
                "time": datetime(2020, 5, 17),
            }
        }


class UpdateTweetModel(BaseModel):
    user_id: Optional[str]
    content: str
    primary_tone: tone.PrimaryTone
    secondary_tones: List[tone.PrimaryTone]
    time: Optional[datetime]

    class Config:
        schema_extra = {
            "example": {
                "user_id": "16f78a7d6317f102bbd95fc9a4f3ff2e3249287690b8bdad6b7810f82b34ace3",
                "content": "I dislike IBM",
                "primary_tone": tone.PrimaryTone.NEGATIVE,
                "secondary_tones": [],
                "time": datetime(2020, 5, 17),
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

from typing import Optional
from pydantic import BaseModel, Field, constr, ValidationError

class TweetSchema(BaseModel):
    user_id: str = Field(...)
    content: str = Field(...)



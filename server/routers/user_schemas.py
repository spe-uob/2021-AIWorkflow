from pydantic import BaseModel


class UserLogInRequest(BaseModel):
    code: str


class UserLogInResponse(BaseModel):
    data: dict
    message: str
    success: bool


class UserLogOutRequest(BaseModel):
    hashed_username: str


class UserLogOutResponse(BaseModel):
    message: str
    success: bool

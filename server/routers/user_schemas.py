from pydantic import BaseModel


class UserLogInRequest(BaseModel):
    code: str


class UserLogInResponse(BaseModel):
    data: dict
    message: str
    success: bool


class UserLogOutRequest(BaseModel):
    user_id: str


class UserLogOutResponse(BaseModel):
    message: str
    success: bool

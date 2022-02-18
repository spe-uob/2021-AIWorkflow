from fastapi import APIRouter, Header
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from .internal.workflow import Workflow
from .user_schemas import (
    UserLogInRequest,
    UserLogInResponse,
    UserLogOutRequest,
    UserLogOutResponse,
)
import os

router = APIRouter(prefix="/user")

load_dotenv(verbose=True)
WORKFLOW_DEMO = Workflow(os.getenv("IBM_TONE_ANALYZER_KEY"))


@router.get("/login", response_model=UserLogInResponse)
async def user_login(request: UserLogInRequest):
    return JSONResponse({"message": "logout successfully"}, status_code=200)


@router.get("/logout", response_model=UserLogOutResponse)
async def user_logout(request: UserLogOutRequest):
    return JSONResponse({"message": "logout successfully"}, status_code=200)

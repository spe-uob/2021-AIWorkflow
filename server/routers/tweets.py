from fastapi import APIRouter, Header
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from .internal.workflow import Workflow
from .tweets_schemas import SaveTweetsRequest, SaveTweetsResponse, SearchTweetsResponse
from .user_schemas import (
    UserLogInRequest,
    UserLogInResponse,
    UserLogOutRequest,
    UserLogOutResponse,
)
from loguru import logger
from traceback import format_exc
import os

router = APIRouter(prefix="/twitterapi")

load_dotenv(verbose=True)
WORKFLOW_DEMO = Workflow(os.getenv("IBM_TONE_ANALYZER_KEY"))


@router.post("/tweets", response_model=SaveTweetsResponse)
async def save_tweet_request(request: SaveTweetsRequest) -> JSONResponse:
    response = {
        "data": {
            "tweet_id": "123456789",
        },
        "message": "saved tweet successfully",
        "success": True,
    }
    return JSONResponse(response, status_code=200)


@router.get("/tweets", response_model=SearchTweetsResponse)
async def search_tweet_request(
    user_id: str,
    keywords: str,
    tones: str,
    time_start: str = None,
    time_end: str = None,
) -> JSONResponse:
    try:
        keywords = [kw.rstrip() for kw in keywords.split(",")]
        tones = [kw.rstrip() for kw in tones.split(",")]
        if WORKFLOW_DEMO.clients.get(user_id) is None:
            return JSONResponse({"message": "User has not logged in"}, status_code=403)

        WORKFLOW_DEMO.main(
            user_id,
            keywords,
            tones,
            time_start,
            time_end,
        )
        response = {
            "data": {},
            "message": "Data is generated, you can see the results on your Google account now.",
            "success": True,
        }
        return JSONResponse(response, status_code=200)
    except Exception as e:
        logger.error(e)
        logger.error(format_exc())
        return JSONResponse({"data": {},"message": "something went wrong", "success": False}, status_code=500)


user_router = APIRouter(prefix="/user")

@user_router.post("/login", response_model=UserLogInResponse)
async def user_login(request: UserLogInRequest):
    logger.debug(request.code)
    user_profile = WORKFLOW_DEMO.authenticate_user("./routers/internal/credentials.json", request.code)
    return JSONResponse({"data": {"google_object": user_profile}, "message": "login successful", "success": True}, status_code=200)

@user_router.get("/")
async def get_users():
    return JSONResponse({"data": {"users": list(WORKFLOW_DEMO.clients.keys())}, "message": "get users successful", "success": True}, status_code=200)


@user_router.post("/logout", response_model=UserLogOutResponse)
async def user_logout(request: UserLogOutRequest):
    logger.debug(request.user_id)
    return JSONResponse({"data": {}, "message": "logout successful", "success": True}, status_code=200)

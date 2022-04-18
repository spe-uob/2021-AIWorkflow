from fastapi import APIRouter, Header, HTTPException, Depends
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from .internal.workflow import Workflow
from .tweets_schemas import (
    SaveTweetsRequest, 
    SaveTweetsResponse, 
    SearchTweetsResponse, 
    TweetRequest, 
    TweetResponse
)
from .database_schemas import (
    GetWorkflowRequest, 
    GetWorkflowResponse
)
from .user_schemas import (
    UserLogInRequest,
    UserLogInResponse,
    UserLogOutRequest,
    UserLogOutResponse,
)
from typing import Optional
from .database import get_collection, retrieve_by_id

from loguru import logger
from traceback import format_exc
import os

load_dotenv(verbose=True)
WORKFLOW = Workflow("./routers/internal/credentials.json", os.getenv("IBM_TONE_ANALYZER_KEY"))

async def get_backend_auth_code(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Missing Authorization Header")
    return authorization

tweet_router = APIRouter(prefix="/twitterapi", dependencies=[Depends(get_backend_auth_code)])

@tweet_router.post("/tweets", response_model=SaveTweetsResponse)
async def save_tweet_request(request: SaveTweetsRequest) -> JSONResponse:
    response = {
        "data": {
            "tweet_id": "123456789",
        },
        "message": "saved tweet successfully",
        "success": True,
    }
    return JSONResponse(response, status_code=200)


@tweet_router.get("/tweets", response_model=SearchTweetsResponse)
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
        if WORKFLOW.clients.get_user(user_id) is None:
            return JSONResponse({"message": "User has not logged in"}, status_code=403)
            
        WORKFLOW.main(
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
    user_profile = WORKFLOW.authenticate_user("./routers/internal/credentials.json", request.code)
    return JSONResponse({"data": {"google_object": user_profile}, "message": "login successful", "success": True}, status_code=200)

@user_router.get("/")
async def get_users(authorization: str = Header(None)):
    if authorization is None or authorization != WORKFLOW.clients:
        raise HTTPException(status_code=401, detail="Missing Authorization Header")
    return JSONResponse({"data": {"users": list(WORKFLOW.clients.keys())}, "message": "get users successful", "success": True}, status_code=200)


@user_router.post("/logout", response_model=UserLogOutResponse)
async def user_logout(request: UserLogOutRequest, authorization: str = Header(None)):
    logger.debug(request.user_id)
    return JSONResponse({"data": {}, "message": "logout successful", "success": True}, status_code=200)

workflow_router = APIRouter(prefix="/workflow", dependencies=[Depends(get_backend_auth_code)])

@workflow_router.get("/")
async def workflow_default():
    return JSONResponse({"data": {}, "message": "get workflow successful", "success": True}, status_code=200)

@workflow_router.post("/run")
async def run_workflow():
    return JSONResponse({"data": {}, "message": "workflow run successful", "success": True}, status_code=200)

database_router = APIRouter(prefix="/database", dependencies=[Depends(get_backend_auth_code)])

@database_router.get("/", response_model=GetWorkflowResponse)
async def database_workflow_get(request: GetWorkflowRequest):
    collection = get_collection("workflows")
    workflow = retrieve_by_id(request.workflow_id, collection)
    return JSONResponse({"data": workflow, "message": "workflow get successful", "success": True}, status_code=200)

@database_router.get("/", response_model=TweetResponse)
async def database_tweet_get(request: TweetRequest):
    collection = get_collection("tweets")
    tweet = retrieve_by_id(request.tweet_id, collection)
    return JSONResponse({"data": tweet, "message": "workflow get successful", "success": True}, status_code=200)

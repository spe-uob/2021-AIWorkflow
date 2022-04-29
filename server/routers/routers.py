from multiprocessing.sharedctypes import Value
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from .internal.workflow import Workflow
from .tweets_schemas import (
    SaveTweetsRequest,
    SaveTweetsResponse,
    SearchTweetsResponse,
    TweetRequest,
    TweetResponse,
)
from .database_schemas import GetWorkflowRequest, GetWorkflowResponse
from .user_schemas import (
    UserLogInRequest,
    UserLogInResponse,
    UserLogOutRequest,
    UserLogOutResponse,
)
from typing import Optional
from .database import get_collection, retrieve_by_id
from .workflow_schemas import WorkflowRun

from loguru import logger
from traceback import format_exc
import os
import json

load_dotenv(verbose=True)

google_creds = "./routers/credentials.json"

with open(google_creds, "r") as f:
    google_creds = json.load(f) 

google_secret=os.getenv("GOOGLE_SECRET")

if google_secret is None:
    raise ValueError("Missing Google Secret")

google_creds["client_secret"]=google_secret

WORKFLOW = Workflow(
    google_creds, os.getenv("IBM_TONE_ANALYZER_KEY")
)

token_auth_scheme = HTTPBearer()


def user_authenticated(auth: str, user_id: str):
    if auth is None:
        raise HTTPException(status_code=401, detail="Missing Authorization Header")
    if WORKFLOW.users.get_user(user_id) is None:
        raise HTTPException(status_code=401, detail="Invalid user")
    if auth != WORKFLOW.users.get_user(user_id).get("code", None):
        raise HTTPException(status_code=401, detail="Unauthorized")
    else:
        return True


tweet_router = APIRouter(prefix="/twitterapi")


@tweet_router.post("/tweets", response_model=SaveTweetsResponse)
async def save_tweet_request(
    request: SaveTweetsRequest, token: str = Depends(token_auth_scheme)
) -> JSONResponse:
    if user_authenticated(token.credentials, request.user_id):
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
    token: str = Depends(token_auth_scheme),
) -> JSONResponse:
    if user_authenticated(token.credentials, user_id):
        try:
            keywords = [kw.rstrip() for kw in keywords.split(",")]
            tones = [kw.rstrip() for kw in tones.split(",")]
            if WORKFLOW.users.get_user(user_id) is None:
                return JSONResponse(
                    {"message": "User has not logged in"}, status_code=403
                )

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
            return JSONResponse(
                {"data": {}, "message": "something went wrong", "success": False},
                status_code=500,
            )


user_router = APIRouter(prefix="/user")


@user_router.post("/login", response_model=UserLogInResponse)
async def user_login(request: UserLogInRequest):
    # no auth because it is a login request
    logger.debug(request.code)
    user_profile = WORKFLOW.user_signin(request.code)
    return JSONResponse(
        {
            "data": {"google_object": user_profile},
            "message": "login successful",
            "success": True,
        },
        status_code=200,
    )


@user_router.get("/")
async def get_users():
    # no auth needed because it only returns public user ids, no private info
    return JSONResponse(
        {
            "data": {"users": list(WORKFLOW.users.get_users().keys())},
            "message": "get users successful",
            "success": True,
        },
        status_code=200,
    )


@user_router.post("/logout", response_model=UserLogOutResponse)
async def user_logout(
    request: UserLogOutRequest, token: str = Depends(token_auth_scheme)
):
    logger.debug(token)
    if user_authenticated(token.credentials, request.user_id):
        WORKFLOW.user_signout(request.user_id)
        return JSONResponse(
            {"data": {}, "message": "logout successful", "success": True},
            status_code=200,
        )


workflow_router = APIRouter(prefix="/workflow")


@workflow_router.get("/")
async def workflow_default():
    return JSONResponse(
        {"data": {}, "message": "workflow router is running", "success": True},
        status_code=200,
    )


@workflow_router.post("/run")
async def run_workflow(r: WorkflowRun, token: str = Depends(token_auth_scheme)):
    if user_authenticated(token.credentials, r.user_id):
        try:
            WORKFLOW.run_workflow(r.user_id, r.workflow)
            return JSONResponse(
                {"data": {}, "message": "workflow run successful", "success": True},
                status_code=200,
            )
        except Exception:
            logger.error(format_exc())
            return JSONResponse(
                {"data": {}, "message": "something went wrong", "success": False},
                status_code=500,
            )


database_router = APIRouter(prefix="/database")


@database_router.get("/", response_model=GetWorkflowResponse)
async def database_workflow_get(
    request: GetWorkflowRequest, token: str = Depends(token_auth_scheme)
):
    if user_authenticated(token.credentials, request.user_id):
        collection = get_collection("workflows")
        workflow = retrieve_by_id(request.workflow_id, collection)
        return JSONResponse(
            {"data": workflow, "message": "workflow get successful", "success": True},
            status_code=200,
        )


@database_router.get("/", response_model=TweetResponse)
async def database_tweet_get(
    request: TweetRequest, token: str = Depends(token_auth_scheme)
):
    if user_authenticated(token.credentials, request.user_id):
        collection = get_collection("tweets")
        tweet = retrieve_by_id(request.tweet_id, collection)
        return JSONResponse(
            {"data": tweet, "message": "workflow get successful", "success": True},
            status_code=200,
        )

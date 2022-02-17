from fastapi import APIRouter, Header
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from .internal.workflow import Workflow
from .tweets_schemas import SaveTweetsRequest, SaveTweetsResponse, SearchTweetsResponse
from loguru import logger
from traceback import format_exc
import os

router = APIRouter(
    prefix="/twitterapi"
)

load_dotenv(verbose=True)
WORKFLOW_DEMO = Workflow(os.getenv('IBM_TONE_ANALYZER_KEY'))


@router.post("/tweets", response_model = SaveTweetsResponse)
async def save_tweet_request(request: SaveTweetsRequest):
    response = {  
    "data": {
      "tweet_id": "123456789",
    },
    "message": "saved tweet successfully",
    "success": True
    }
    return JSONResponse(response, status_code = 200)
 
@router.get("/tweets", response_model = SearchTweetsResponse)
async def search_tweet_request(user_id: str, keywords: str, tones: str, time_start: str = None, time_end: str = None, code : str = Header(None)):
    try:
        keywords = [kw.rstrip() for kw in keywords.split(",")]
        tones = [kw.rstrip() for kw in tones.split(",")]
        if code is None:
            return JSONResponse({"message": "token is required"}, status_code = 401)
        
        WORKFLOW_DEMO.main("./routers/internal/credentials.json", code, user_id, keywords, tones, time_start, time_end)
        response = {
            "data": {},
            "message": "Data is generated, you can see the results on your Google account now.",
            "success": True
        }
        return JSONResponse(response, status_code = 200)
    except Exception as e:
        logger.error(e)
        logger.error(format_exc())
        return JSONResponse({"message": "something went wrong"}, status_code = 500)

from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from .internal.workflow import Workflow
from .tweets_schemas import SaveTweetsRequest, SaveTweetsResponse, SearchTweetsResponse

router = APIRouter(
    prefix="/twitterapi"
)

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
async def search_tweet_request(user_id: str, keywords: str, tones: str, time_start: str = None, time_end: str = None, token : str = Header(None)):
    keywords = [kw.rstrip() for kw in keywords.split(",")]
    tones = [kw.rstrip() for kw in tones.split(",")]
    if token is None:
        return JSONResponse({"message": "token is required"}, status_code = 401)
    workflow_demo = Workflow(token)
    workflow_demo.main(user_id, keywords, tones, time_start, time_end)
    response = {
        "data": {},
        "message": "Data is generated, you can see the results on your Google account now.",
        "success": True
    }
    return JSONResponse(response, status_code = 200)
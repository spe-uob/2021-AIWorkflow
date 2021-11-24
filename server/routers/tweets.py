from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .tweets_schemas import SaveTweetsRequest, SaveTweetsResponse, SearchTweetsResponse, SearchTweetsRequest

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
async def search_tweet_request(request: SearchTweetsRequest):
    response = {  
    "data": {
      "tweets": [
        {
          "text": "I love IBM",
          "url": "https:/twitter.com/id/8013879718"
        },
        {
          "text": "I dislike IBM",
          "url": "https:/twitter.com/id/231233217"
        }
      ],
    },
    "message": "searched tweet successfully",
    "success": True
    }
    return JSONResponse(response, status_code = 200)
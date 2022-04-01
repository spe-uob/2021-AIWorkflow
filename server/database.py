import motor.motor_asyncio
import json

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.ibm
tweet_collection = database.get_collection("tweets")
workflow_collection = database.get_collection("workflows")

def get_collection(name):
    if name == "tweets":
        return tweet_collection
    elif name == "workflows":
        return workflow_collection
    else:
        raise NotImplementedError("Unknown collection")

def tweet_helper(tweet) -> dict:
    return {
        "id": str(tweet["_id"]),
        "user_id": tweet["user_id"],
        "content": tweet["content"],
        "primary_tone": tweet["primary_tone"],
        "secondary_tones": tweet["secondary_tones"],
        "time": tweet["time"],
    }

# Use [tweet_helper(tweet) for tweet in retrieve_all_from_collection(tweet_collection)] to get all tweets
async def retrieve_all_from_collection(collection: motor.motor_asyncio.AsyncIOMotorCollection) -> List[dict]:
    items = []
    async for item in collection.find():
        items.append(item)
    return items

# Use json.loads() to convert json string to dict
async def add_to_collection(data: dict, collection: motor.motor_asyncio.AsyncIOMotorCollection) -> dict:
    item = await collection.insert_one(data)
    new_data = await collection.find_one({"_id": item.inserted_id})
    return new_data

async def retrieve_by_id(in_id: int, collection: motor.motor_asyncio.AsyncIOMotorCollection) -> dict:
    item = await collection.find_one({"_id": in_id})
    return item

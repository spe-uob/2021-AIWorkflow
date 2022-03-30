import motor.motor_asyncio
import json

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.ibm
tweet_collection = database.get_collection("tweets")
print(type(tweet_collection))
workflow_collection = database.get_collection("workflows")

def tweet_helper(tweet) -> dict:
    return {
        "id": str(tweet["_id"]),
        "user_id": tweet["user_id"],
        "content": tweet["content"],
        "primary_tone": tweet["primary_tone"],
        "secondary_tones": tweet["secondary_tones"],
        "time": tweet["time"],
    }

async def retrieve_all_tweets() -> dict:
    tweets = []
    async for tweet in tweet_collection.find():
        tweets.append(tweet_helper(tweet))
    return tweets

# Use json.loads() to convert json string to dict
async def add_to_collection(data: dict, collection: motor.motor_asyncio.AsyncIOMotorCollection) -> dict:
    item = await collection.insert_one(data)
    new_data = await collection.find_one({"_id": item.inserted_id})
    return new_data
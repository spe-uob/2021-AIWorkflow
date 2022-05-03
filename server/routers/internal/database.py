from typing import List
import motor.motor_asyncio
import asyncio
import os

environment = os.getenv("ENVIRONMENT", "development")
if environment == "development":
    MONGO_DETAILS = "mongodb://dongo:27017"
else:
    MONGO_DETAILS = "mongodb://172.21.208.59:27017"
print(MONGO_DETAILS)
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
client.get_io_loop = asyncio.get_running_loop
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
async def retrieve_all_from_collection(
    collection: motor.motor_asyncio.AsyncIOMotorCollection,
) -> List[dict]:
    items = [item async for item in collection.find()]
    return items


# Use json.loads() to convert json string to dict
async def add_to_collection(
    data: dict, collection: motor.motor_asyncio.AsyncIOMotorCollection
) -> dict:
    item = await collection.insert_one(data)
    new_data = await collection.find_one({"_id": item.inserted_id})
    return new_data


async def retrieve_by_id(
    in_id: int, collection: motor.motor_asyncio.AsyncIOMotorCollection
) -> dict:
    item = await collection.find_one({"_id": in_id})
    return item


async def retrieve_by_user_id(
    user_id: str, collection: motor.motor_asyncio.AsyncIOMotorCollection
) -> dict:
    items = [item async for item in collection.find({"user_id": user_id})]
    for item in items:
        item["_id"] = str(item["_id"])
    return items


async def test():
    result = await retrieve_all_from_collection(get_collection("tweets"))
    return result


if __name__ == "__main__":
    print(asyncio.run(test()))

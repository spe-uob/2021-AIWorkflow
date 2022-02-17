import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.ibm
tweet_collection = database.get_collection("tweets")


def tweet_helper(tweet) -> dict:
    return {
        "id": str(tweet["_id"]),
        "user_id": tweet["user_id"],
        "content": tweet["content"],
        "primary_tone": tweet["primary_tone"],
        "secondary_tones": tweet["secondary_tones"],
        "time": tweet["time"],
    }


async def retrieve_all_tweets():
    tweets = []
    async for tweet in tweet_collection.find():
        tweets.append(tweet_helper(tweet))
    return tweets


async def add_tweet(tweet_data: dict) -> dict:
    tweet = await tweet_collection.insert_one(tweet_data)
    new_tweet = await tweet_collection.find_one({"_id": tweet.inserted_id})
    return tweet_helper(new_tweet)

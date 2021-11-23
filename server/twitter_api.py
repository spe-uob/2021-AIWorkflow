import tweepy as tw
from tweepy.errors import *
from typing import List, Dict, Optional
from dotenv import load_dotenv
from loguru import logger
import os

class TwitterAPI:

    def __init__(self) -> None:
        load_dotenv(verbose=True)
        logger.debug(os.getenv("TWITTER_API_BEARER_TOKEN"))
        self.twitter_api = tw.Client(bearer_token=os.getenv("TWITTER_API_BEARER_TOKEN"))

    def search_tweets(self, keywords: List[str], start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict[str, str]]:
        logger.debug(f"Searching tweets for keywords: {keywords}")
        tweets = []
        try:
            tweets = self.twitter_api.search_all_tweets(
                query = ", ".join(keywords),
                start_time = start_date,
                end_time = end_date
            )
        except Forbidden:
            logger.error(f"Error searching tweets: Forbidden")
        finally:
            return tweets


if __name__ == '__main__':
    twitterapi_istance = TwitterAPI()
    logger.debug(twitterapi_istance.search_tweets(["awesome"]))
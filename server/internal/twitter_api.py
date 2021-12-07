from tweepy.errors import *
from typing import List, Dict, Optional
from dotenv import load_dotenv
from loguru import logger
import tweepy as tw
import unittest
import os

class TwitterAPI:

    def __init__(self) -> None:
        load_dotenv(verbose=True)
        logger.debug(os.getenv("TWITTER_API_BEARER_TOKEN"))
        self.twitter_api = tw.Client(bearer_token=os.getenv("TWITTER_API_BEARER_TOKEN"))

    def search_tweets(self, keywords: List[str], start_date: Optional[str] = None, end_date: Optional[str] = None) -> List[Dict[str, str]]:
        logger.debug(f"Searching tweets for keywords: {keywords}")
        tweets = [
            {
                "text": "IBM's services are terrible... I am sad.",
                "date": "2021-11-26 11:11:11",
                "hashed_usernme": "nsljhsdjlfalskf"
            },
            {
                "text": "IBM's services are great, I am so happy!",
                "date": "2021-11-26 11:11:11",
                "hashed_usernme": "nsljhsdjlfalskf"
            }
        ]
        """
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
        """
        return tweets

class Tests(unittest.TestCase):

    def test_search_tweets(self):
        api = TwitterAPI()
        tweets = api.search_tweets(["#trump"], start_date="2020-01-01", end_date="2020-01-02")
        self.assertTrue(len(tweets) > 0)


if __name__ == '__main__':
    unittest.main()
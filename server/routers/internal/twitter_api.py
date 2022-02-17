from loguru import logger
from pprint import pprint
from hashlib import sha256
from snscrape.modules.twitter import TwitterSearchScraper
from typing import Optional, List, Dict
import unittest
import os


class TwitterAPI:
    def __init__(self) -> None:
        pass

    """
    def search_tweets(self, query_text, start_date, end_date): 
        result = []
        for text in query_text:
            query = f"{text} since:{start_date} until:{end_date}"
            logger.info(f"Searching tweets with query: {query}")
            for tweet in TwitterSearchScraper(query).get_items():
                hashed_username = sha256(tweet.user.username.encode('utf-8')).hexdigest()
                result.append({"text": tweet.content, "date": tweet.date.strftime("%Y-%m-%d %H:%M"), "hashed_username": hashed_username})

        print(result)
        return result
    """

    def search_tweets(
        self,
        keywords: List[str],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> List[Dict[str, str]]:
        logger.debug(f"Searching tweets for keywords: {keywords}")
        tweets = [
            {
                "text": "IBM's VPCs services are terrible... I am sad.",
                "date": "2021-11-26 11:11:11",
                "hashed_usernme": "nsljhsdjlfalskf",
            },
            {
                "text": "I am so excited to celebrate the joyous occasion that my application is now running on IBM Watson!",
                "date": "2021-11-26 11:11:11",
                "hashed_usernme": "13890bjkdsv",
            },
            {
                "text": "I am so frustrated IBM... I am angry!",
                "date": "2021-11-26 11:11:11",
                "hashed_usernme": " ;gklhfsg",
            },
            {
                "text": "text",
                "date": "2021-11-26 11:11:11",
                "hashed_usernme": " ;gklhfsg",
            },
        ]
        return tweets


class Tests(unittest.TestCase):
    def test_search_tweets(self):
        api = TwitterAPI()
        tweets = api.search_tweets(
            ["#ibmcloud"], start_date="2020-01-01", end_date="2020-01-02"
        )
        self.assertTrue(len(tweets) > 0)


if __name__ == "__main__":
    unittest.main()

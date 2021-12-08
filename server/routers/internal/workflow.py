from .google_slides import GoogleSlides
from .google_sheets import GoogleSheets
from .tone_analyzer import IBMToneAnalyzer
from .twitter_api import TwitterAPI
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional
from loguru import logger
from datetime import datetime
import os


class Workflow:

    def __init__(self, google_creds: dict = None) -> None:
        self.twitterapi = TwitterAPI()
        self.toneanalyzer = IBMToneAnalyzer()
        self.googleslides = GoogleSlides(google_creds)
        self.googlesheets = GoogleSheets(google_creds)

    def main(self, user_id: str, keywords: List[str], tones: List[str], start_date: Optional[str] = None, end_date: Optional[str] = None):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        tweets = self.twitterapi.search_tweets(keywords, start_date, end_date)        

        self.googlesheets.add_tweets_to_spreadsheet(tweets, date)

        for tweet in tweets:
            #{'text': "I'm so happy today!", 'primary_tone': 'positive', 'tones': ['joy']}
            tweet_analysis = self.toneanalyzer.get_analysis(text = tweet["text"])
            primary_tone = tweet_analysis["primary_tone"]
            tweet.update({"primary_tone": primary_tone})
        
        logger.debug(tweets)

        #TODO sort tweets into positive and negative tones
        processed_tweets = {}
        for tweet in tweets:
            if tweet["primary_tone"] in tones:
                processed_tweets.update({tweet["primary_tone"]: []})
        for tweet in tweets:
            if tweet["primary_tone"] in tones:
                processed_tweets[tweet["primary_tone"]].append(tweet)
            
            
        logger.debug(processed_tweets)

        #TODO add into google slides e.g. self.googleslides.add_tweets_to_slides(...)
        for primary_tone, tweets_with_tone in processed_tweets.items():
            self.googleslides.add_tweets_to_slide(tweets_with_tone, date, primary_tone)
            
            


if __name__ == '__main__':
    wf = Workflow()
    wf.main("ibm", ["ibm"], ["happy", "sad"])

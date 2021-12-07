from re import T
from google_slides import GoogleSlides
from google_sheets import GoogleSheets
from server.internal.google_slides import main
from tone_analyzer import IBMToneAnalyzer
from twitter_api import TwitterAPI
from typing import List, Dict, Optional
from datetime import datetime


class Workflow:

    def __init__(self) -> None:
        self.twitterapi = TwitterAPI()
        self.toneanalyzer = IBMToneAnalyzer()
        self.googleslides = GoogleSlides()
        self.googlesheets = GoogleSheets()

    def main(self, user_id: str, keywords: List[str], tones: List[str], start_date: Optional[str] = None, end_date: Optional[str] = None):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        tweets = self.twitterapi.search_tweets(user_id, keywords, tones, start_date, end_date)
        """
        tweets = [
            {
                "text": "IBM sucks",
                "time": "2021-11-26 11:11:11",
                "hashed_usernme": "nsljhsdjlfalskf"
            }
        ]
        """

        #TODO add into google sheets e.g. self.googlesheets.add_tweets_to_sheet(...)

        
        self.googlesheets.add_tweets_to_spreadsheet(tweets, date, tones)

        for tweet in tweets:
            tweettone = self.toneanalyzer.get_analysis(text = tweet["text"])
            tweet.update({"tone": tweettone})

        """
        tweets = [
            {
                "text": "ibm",
                "time": "",
                "hashed_username": "",
                "tone": ""
            }
        ]
        """

        

        """save to database:
        {
            "username": "ibm",
            "token": "",
            "tweets": tweets
        }
        """

        #TODO sort tweets into positive and negative tones
        temp = {}
        for tweet in tweets:
            temp.update({tweets["tone"]: []})
        for tweet in tweets:
            temp[tweets["tone"]].append(tweet)
            

        """
        {
            "happy": [
                {
                    "text": "ob....".
                    .
                    .
                }
            ],
            "sad": [
                .
                .
                .
            ]
        }
        """


        #TODO add into google slides e.g. self.googleslides.add_tweets_to_slides(...)
        for tone, tweets_with_tone in enumerate(temp):
            self.googleslides.add_tweets_to_slide(tweets_with_tone, date, tone)


if __name__ == '__main__':
    wf = Workflow()

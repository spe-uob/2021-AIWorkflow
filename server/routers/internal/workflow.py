from .google_slides import GoogleSlides
from .google_sheets import GoogleSheets
from .tone_analyzer import IBMToneAnalyzer
from .twitter_api import TwitterAPI
from .google_api import GoogleAPI
from typing import List, Optional
from loguru import logger
from datetime import datetime

class Workflow:
    def __init__(self, ibm_ta_key: str) -> None:
        self.twitterapi = TwitterAPI()
        self.toneanalyzer = IBMToneAnalyzer(ibm_ta_key)
        self.clients = {}

    def main(
        self,
        creds_file: str,
        google_api_auth_code: str,
        user_id: str,
        keywords: List[str],
        tones: List[str],
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ):
        # TODO UPDATE DOCS
        logger.warning(self.clients.get(user_id))
        if self.clients.get(user_id) is None:
            google_creds = GoogleAPI(creds_file, google_api_auth_code).credentials
            googleslides = GoogleSlides(google_creds)
            googlesheets = GoogleSheets(google_creds)
            self.clients.update(
                {
                    user_id: {
                        "googleslides": googleslides,
                        "googlesheets": googlesheets,
                    }
                }
            )

        else:
            googleslides = self.clients[user_id]["googleslides"]
            googlesheets = self.clients[user_id]["googlesheets"]

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        tweets = self.twitterapi.search_tweets(keywords, start_date, end_date)

        googlesheets.add_tweets_to_spreadsheet(tweets, date)

        for tweet in tweets:
            # {'text': "I'm so happy today!", 'primary_tone': 'positive', 'tones': ['joy']}
            tweet_analysis = self.toneanalyzer.get_analysis(text=tweet["text"])
            primary_tone = tweet_analysis["primary_tone"]
            tweet.update({"primary_tone": primary_tone})

        logger.debug(tweets)

        # TODO sort tweets into positive and negative tones
        processed_tweets = {}
        for tweet in tweets:
            if tweet["primary_tone"] in tones:
                processed_tweets.update({tweet["primary_tone"]: []})
        for tweet in tweets:
            if tweet["primary_tone"] in tones:
                processed_tweets[tweet["primary_tone"]].append(tweet)

        logger.debug(processed_tweets)

        # TODO add into google slides e.g. self.googleslides.add_tweets_to_slides(...)
        for primary_tone, tweets_with_tone in processed_tweets.items():
            googleslides.add_tweets_to_slide(tweets_with_tone, date, primary_tone)

        logger.debug(self.clients)


if __name__ == "__main__":
    wf = Workflow()
    wf.main("ibm", ["ibm"], ["happy", "sad"])

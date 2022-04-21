from multiprocessing.sharedctypes import Value
from .tone_analyzer import IBMToneAnalyzer
from .twitter_api import TwitterAPI
from .users import Users
from typing import List, Optional, Dict
from loguru import logger
from datetime import datetime
from traceback import format_exc

class Workflow:
    def __init__(self, google_creds_file: str, ibm_ta_key: str) -> None:
        self.creds_file = google_creds_file
        self.users = Users()
        self.twitter_api = TwitterAPI()
        self.tone_analyzer = IBMToneAnalyzer(ibm_ta_key)

    def user_signout(self, user_id: str) -> None:
        self.users.remove_user(user_id)

    def user_signin(self, auth_code: str) -> dict:
        try:
            return self.users.register_user(self.creds_file, auth_code)
        except Exception as e:
            logger.error(e)
            logger.error(format_exc())

    def run(self, user_id: str, backend_auth_code: str, workflow_request: Dict[str ,str]) -> None:
        user_profile = self.users.get_user(user_id)
        if user_profile is None:
            raise ValueError("User not found")
        elif backend_auth_code != self.users.get_users["code"]:
            print("Auth_key incorrect!")
        else:
            self.parse_workflow(workflow_request)
  
    def parse_workflow(self, backend_auth_code: str, workflow_request: Dict[str, str]) -> None:
        workflow_request = workflow_request["nodes"]
        for id, node in workflow_request.items():
            #print(id, node)
            if node["name"] == "Search Twitter":
                keywords = node["data"]["keywords"]
                tweets = self.twitter_api.search_tweets(keywords)
        
            if node["name"] == "Tone Analyzer":
                for tweet in tweets:
                    tweet_analysis = self.tone_analyzer.get_analysis(text=tweet["text"])
                    primary_tone = tweet_analysis["primary_tone"]
                    tweet.update({"primary_tone": primary_tone})
                    print("primary_tone")
            if node["name"] == "Write to google sheets":
                print('writing to google sheets')
            if node["name"] == "Write to google slides":
                print('writing to google slides')

    def automation(
        
    )


    def main(
            self,
            user_id: str,
            keywords: List[str],
            tones: List[str],
            start_date: Optional[str] = None,
            end_date: Optional[str] = None,
        ) -> None:
            if self.users.get_user(user_id) is None:
                raise ValueError("User has not logged in yet.")

            googlesheets = self.users.get_user(user_id).get("googlesheets")
            googleslides = self.users.get_user(user_id).get("googleslides")

            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")     

            tweets = self.twitter_api.search_tweets(keywords, start_date, end_date)

            googlesheets.add_tweets_to_spreadsheet(tweets, date)

            for tweet in tweets:
                # {'text': "I'm so happy today!", 'primary_tone': 'positive', 'tones': ['joy']}
                tweet_analysis = self.tone_analyzer.get_analysis(text=tweet["text"])
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
    wf = Workflow("T2aP_uwW5D08F7pBtyvuZVuCRm1QGPXgm6qASB-JKyR")
    #wf.main("ibm", ["ibm"], ["happy", "sad"])
    wf.authenticate_user("./credentials.json", "4/0AX4XfWjOZFSsCSOYjfa5Dv4I4kIJjfBu6GhRd4KBwiPE4MiBZFKUzEggTHi6rmcTv-ExaQ\\")

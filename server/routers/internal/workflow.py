from .tone_analyzer import IBMToneAnalyzer
from .twitter_api import TwitterAPI
from .users import Users
from typing import List, Optional, Dict
from loguru import logger
from datetime import datetime
from traceback import format_exc
import threading

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
  
    def run_workflow(self, user_id: str, workflow: Dict[str, str]) -> None:
        logger.debug(workflow)
        workflow_variables = {}
        nodes = workflow["nodes"]
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        googlesheets = self.users.get_user(user_id).get("googlesheets")
        googleslides = self.users.get_user(user_id).get("googleslides")
        for _, node in nodes.items():
            print("")
            #print(num, node)
            if node["data"]:
                workflow_variables.update(node["data"])
            #print(node["data"])
            if node["name"] == "Search Twitter":
                logger.debug("searching twitter.")
                output_var = list(node["outputs"].keys())[0]
                tweets = self.twitter_api.search_tweets(node["data"]["keywords"])
                workflow_variables.update({output_var : tweets})
                logger.debug(f"searched: {tweets}")
            if node["name"] == "Tone Analyzer":
                logger.debug("tone")
                input_var = list(node["inputs"].keys())[0]
                data = workflow_variables[input_var]
                for datum in data:
                    # {'text': "I'm so happy today!", 'primary_tone': 'positive', 'tones': ['joy']}
                    analysis = self.tone_analyzer.get_analysis(text=datum["text"])
                    primary_tone = analysis["primary_tone"]
                    datum.update({"primary_tone": primary_tone})
                output_var = list(node["outputs"].keys())[0]
                workflow_variables.update({output_var: tweets})
                logger.debug(f"tone_analyser: {tweets}")
            if node["name"] == "Write to Google Sheets":
                logger.debug('writing to google sheets')
                input_var = list(node["inputs"].keys())[0]
                data = workflow_variables[input_var]
                googlesheets.add_tweets_to_spreadsheet(data, date)
                logger.debug(f"write_data GSheets: {data}")
            if node["name"] == "Write to Google Slides":
                logger.debug('writing to google slides')
                input_var = list(node["inputs"].keys())[0]
                data = workflow_variables[input_var]
                tones = []
                if workflow_variables.get("positive") is True:
                    tones.append("Positive")
                if workflow_variables.get("negative") is True:
                    tones.append("Negative")
                processed_data = {}
                for datum in data:
                    if datum["primary_tone"] in tones:
                        processed_data.update({datum["primary_tone"]: []})
                for datum in data:
                    if datum["primary_tone"] in tones:
                        processed_data[datum["primary_tone"]].append(datum)
                logger.info(processed_data)
                for primary_tone, i in processed_data.items():
                    googleslides.add_tweets_to_slide(i, date, primary_tone)
                logger.debug(f"write_data GSlides: {data}")
        return

    def automation(self, workflow_request: Dict[str, str]) -> None:
        thread1 = threading.Timer(interval= 3600, function= self.run, args=(workflow_request))
        thread1.start()

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


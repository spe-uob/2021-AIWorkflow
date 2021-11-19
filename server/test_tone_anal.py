from ibm_watson import ToneAnalyzerV3
from dotenv import load_dotenv
import os
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator

class ToneAnalyzerSPE:
    def __init__(self) -> None:
        load_dotenv()
        self.authenticator = IAMAuthenticator(os.environ['KEY'])
        self.tone_analyzer = ToneAnalyzerV3(
            version='2017-09-21',
            authenticator=self.authenticator
        )
        self.tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/cacd7ebe-969c-4c32-a8e3-fb03cdedb442')

    def get_analysis(self, text: str) -> dict:

        return self.tone_analyzer.tone(
            {'text':text},
            content_type = 'application/json',
            sentences=False
        ).get_result()

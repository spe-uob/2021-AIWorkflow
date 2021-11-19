from ibm_watson import ToneAnalyzerV3
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from loguru import logger
import os

class IBMToneAnalyzer:
    def __init__(self) -> None:
        logger.info("IBMToneAnalyzer __init__()")
        load_dotenv()
        self.authenticator = IAMAuthenticator(os.getenv('IBM_TONE_ANALZER_KEY'))
        self.tone_analyzer = ToneAnalyzerV3(
            version='2017-09-21',
            authenticator=self.authenticator
        )
        self.tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/cacd7ebe-969c-4c32-a8e3-fb03cdedb442')

    def get_analysis(self, text: str) -> dict:
        logger.info(f"IBMToneAnalyzer.get_analysis(text: {text})")
        analysis = self.tone_analyzer.tone(
            {'text':text},
            content_type = 'application/json',
            sentences=False
        ).get_result()
        logger.debug(f"Analysis: {analysis}")
        return analysis

if __name__ == '__main__':
    ibm_ta_instance = IBMToneAnalyzer()
    ibm_ta_instance.get_analysis("I am very angry")
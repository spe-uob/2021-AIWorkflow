from ibm_watson import ToneAnalyzerV3
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from loguru import logger
import unittest
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
        #TODO RETURN MORE THAN ONE TONE ANALYSIS
        logger.info(f"IBMToneAnalyzer.get_analysis(text: {text})")
        analysis = self.tone_analyzer.tone(
            {'text':text},
            content_type = 'application/json',
            sentences=False
        ).get_result()
        logger.debug(f"Analysis: {analysis}")
        return analysis["document_tone"]["tones"][0]["tone_id"]

class Tests(unittest.TestCase):

    def test_get_analysis(self):
        tone_analyzer_instance = IBMToneAnalyzer()
        analysis = tone_analyzer_instance.get_analysis("I'm so happy today!")
        tones = [x['tone_id'] for x in analysis['document_tone']['tones']]
        self.assertTrue('joy' in tones)

if __name__ == '__main__':
    unittest.main()
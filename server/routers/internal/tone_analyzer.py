from json import load
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from loguru import logger
from os import getenv
from dotenv import load_dotenv
import unittest


class IBMToneAnalyzer:
    def __init__(self, key: str) -> None:
        logger.info(f"IBMToneAnalyzer __init__({key})")

        self.authenticator = IAMAuthenticator(key)
        self.tone_analyzer = ToneAnalyzerV3(
            version="2017-09-21", authenticator=self.authenticator
        )
        self.tone_analyzer.set_service_url(
            "https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/cacd7ebe-969c-4c32-a8e3-fb03cdedb442"
        )
        self.POSITIVE_TONES = ["joy"]
        self.NEGATIVE_TONES = ["anger", "fear", "sadness"]

    def get_analysis(self, text: str) -> dict:
        logger.info(f"IBMToneAnalyzer.get_analysis(text: {text})")
        analysis = self.tone_analyzer.tone(
            {"text": text}, content_type="application/json", sentences=False
        ).get_result()
        logger.debug(f"Analysis: {analysis}")
        found_tones = analysis["document_tone"]["tones"]
        if found_tones:
            tones = [x["tone_id"] for x in found_tones]
            primary_tone = found_tones[0]["tone_id"]
            if primary_tone in self.POSITIVE_TONES:
                primary_tone = "Positive"
            elif primary_tone in self.NEGATIVE_TONES:
                primary_tone = "Negative"
            else:
                primary_tone = ""
            analysis = {"text": text, "primary_tone": primary_tone, "tones": tones}
        else:
            analysis = {"text": text, "primary_tone": "", "tones": []}
        return analysis


class Tests(unittest.TestCase):
    def test_get_analysis(self) -> None:
        load_dotenv(verbose=True)
        tone_analyzer_instance = IBMToneAnalyzer(getenv("IBM_TONE_ANALYZER_KEY"))
        analysis = tone_analyzer_instance.get_analysis("I'm so happy today!")
        logger.debug(f"analysis: {analysis}")


if __name__ == "__main__":
    unittest.main()

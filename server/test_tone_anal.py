from ibm_watson import ToneAnalyzerV3
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator

authenticator = IAMAuthenticator('_T2aP_uwW5D08F7pBtyvuZVuCRm1QGPXgm6qASB-JKyR')
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/cacd7ebe-969c-4c32-a8e3-fb03cdedb442')

text = 'IBM is the worst company on the planet! Their products are very bad, and the website is impossible to navigate. Why are they not bankrupt yet?'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json'
).get_result()

print(json.dumps(tone_analysis, indent=2))

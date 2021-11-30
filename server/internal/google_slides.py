from __future__ import print_function
from google_drive import GoogleDrive
from typing import List, Dict
from loguru import logger

# If modifying these scopes, delete the file token.json.
SCOPES = [
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/drive",
]


class GoogleSlides(GoogleDrive):
    def create_presentation(self, body) -> str:
        presentation = self.slides_service.presentations().create(body=body).execute()
        return presentation.get("presentationId")

    def create_tweet_slide(self, presentation_id: str, text: str, date_posted: str):
        presentation = (
            self.slides_service.presentations()
            .get(presentationId=presentation_id)
            .execute()
        )
        num_of_slides = len(presentation.get("slides"))
        pt350 = {"magnitude": 350, "unit": "PT"}
        new_slide_request = [
            {
                "createSlide": {
                    "insertionIndex": f"{num_of_slides}",
                    "slideLayoutReference": {"predefinedLayout": "BLANK"},
                }
            }
        ]
        body = {"requests": new_slide_request}
        response = (
            self.slides_service.presentations()
            .batchUpdate(presentationId=presentation_id, body=body)
            .execute()
        )
        create_slide_response = response.get("replies")[0].get("createSlide")
        page_id = create_slide_response.get("objectId")
        element_id = f"{page_id}_tweetbox"
        new_tweetbox_request = [
            {
                "createShape": {
                    "objectId": element_id,
                    "shapeType": "TEXT_BOX",
                    "elementProperties": {
                        "pageObjectId": page_id,
                        "size": {"height": pt350, "width": pt350},
                        "transform": {
                            "scaleX": 1,
                            "scaleY": 1,
                            "translateX": 150,
                            "translateY": 150,
                            "unit": "PT",
                        },
                    },
                }
            },
            {
                "insertText": {
                    "objectId": element_id,
                    "insertionIndex": 0,
                    "text": f"Text: {text}\n\nDate posted: {date_posted}",
                }
            },
        ]
        body = {"requests": new_tweetbox_request}
        response = (
            self.slides_service.presentations()
            .batchUpdate(presentationId=presentation_id, body=body)
            .execute()
        )
        create_shape_response = response.get("replies")[0].get("createShape")
        print(
            "Created textbox with ID: {0}".format(create_shape_response.get("objectId"))
        )

    def add_tweets_to_slide(
        self,
        tweets: List[Dict[str, str]],
        date: str,
        tone: str,
        presentation_id: str = None,
    ):
        if presentation_id is None:
            body = {"title": f"tweets - {tone} - {date}"}
            presentation_id = self.create_presentation(body)
        logger.debug(f"presentation_id: {presentation_id}")
        for tweet in tweets:
            self.create_tweet_slide(presentation_id, tweet["text"], tweet["date"])


if __name__ == "__main__":
    gsinstance = GoogleSlides()
    gsinstance.add_tweets_to_slide(
        [
            {"text": "IBM Cloud is so great!", "date": "2021-11-20"},
            {"text": "IBM Cloud is amazing - great customer service!", "date": "2021-11-3"},
            {"text": "I fucking love coffee - great way to start the morning!", "date": "2021-11-5"}
        ],
        "2021-11-29",
        "joy"
    )

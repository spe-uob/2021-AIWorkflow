from __future__ import print_function
from .google_drive import GoogleDrive
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from typing import List, Dict
from loguru import logger


class GoogleSlides(GoogleDrive):
    def __init__(self, creds: Credentials) -> None:
        super().__init__(creds)
        self.slides_service = build("slides", "v1", credentials=creds)

    def get_all_presentations(self) -> list:
        return self.get_all_files("application/vnd.google-apps.presentation")

    def create_presentation(self, body) -> str:
        presentation = self.slides_service.presentations().create(body=body).execute()
        return presentation.get("presentationId")

    def create_tweet_slide(
        self, presentation_id: str, text: str, date_posted: str
    ) -> None:
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
                    "text": f'"{text}"\n\nDate posted: {date_posted}',
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
        logger.info(
            f"Created textbox with ID: {format(create_shape_response.get('objectId'))}"
        )

    def add_tweets_to_slide(
        self,
        tweets: List[Dict[str, str]],
        date: str,
        tone: str,
        presentation_id: str = None,
    ) -> None:
        if presentation_id is None:
            body = {"title": f"Tweets - {tone} - {date}"}
            presentation_id = self.create_presentation(body)
        logger.debug(f"presentation_id: {presentation_id}")
        for tweet in tweets:
            self.create_tweet_slide(presentation_id, tweet["text"], tweet["date"])


if __name__ == "__main__":
    gslidesinstance = GoogleSlides()
    gslidesinstance.add_tweets_to_slide(
        [
            {"text": "This is awesome!", "date": "2021-11-20"},
            {"text": "IBM Cloud is amazing", "date": "2021-11-20"},
            {"text": "Love the new IBM VPC servers.", "date": "2021-11-20"},
            {"text": "awesome text", "date": "2021-11-20"},
        ],
        "2021-11-29",
        "joy",
    )

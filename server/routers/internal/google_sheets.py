from __future__ import print_function
from google_drive import GoogleDrive
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from typing import List, Dict
from loguru import logger


TWITTER_HEADERS = ["Text", "POST DATE"]
TWITTER_RANGE = "A1:B1"


class GoogleSheets(GoogleDrive):
    def __init__(self, creds: Credentials) -> None:
        super().__init__(creds)
        self.sheets_service = build("sheets", "v4", credentials=creds)

    def create_spreadsheet(
        self, body: str, headers: List[str], range: str, value_input_option: str
    ) -> int:
        spreadsheet = (
            self.sheets_service.spreadsheets()
            .create(body=body, fields="spreadsheetId")
            .execute()
        )
        sheet_id = spreadsheet.get("spreadsheetId")
        body = {"values": [headers]}
        self.sheets_service.spreadsheets().values().update(
            spreadsheetId=sheet_id,
            range=range,
            valueInputOption=value_input_option,
            body=body,
        ).execute()
        return sheet_id

    def add_tweets(
        self,
        sheet_id: str,
        tweets: List[Dict[str, str]],
        range: str,
        value_input_option: str,
    ) -> None:
        insert_data_option = "INSERT_ROWS"  # TODO: Update placeholder value.
        value_range_body = {"values": []}
        for tweet in tweets:
            value_range_body["values"].append([tweet["text"], tweet["date"]])
        self.sheets_service.spreadsheets().values().append(
            spreadsheetId=sheet_id,
            range=range,
            valueInputOption=value_input_option,
            insertDataOption=insert_data_option,
            body=value_range_body,
        ).execute()

    def add_tweets_to_spreadsheet(
        self,
        tweets: List[Dict[str, str]],
        date: str,
        tone: str = None,
        sheet_id: str = None,
    ) -> None:
        if tone is None:
            tone = "General"
        if sheet_id is None:
            body = {"properties": {"title": f"Tweets - {tone} - {date}"}}
            sheet_id = self.create_spreadsheet(
                body, TWITTER_HEADERS, TWITTER_RANGE, "RAW"
            )
        logger.debug(f"presentation_id: {sheet_id}")
        self.add_tweets(sheet_id, tweets, TWITTER_RANGE, "RAW")


if __name__ == "__main__":
    gsheetsinstance = GoogleSheets()
    gsheetsinstance.add_tweets_to_spreadsheet(
        [
            {"text": "This is awesome!", "date": "2021-11-20"},
            {"text": "IBM Cloud is amazing", "date": "2021-11-20"},
            {"text": "Love the new IBM VPC servers.", "date": "2021-11-20"},
            {"text": "awesome text", "date": "2021-11-20"},
        ],
        "2021-11-29",
        "joy",
    )

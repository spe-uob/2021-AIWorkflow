from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from loguru import logger


class GoogleDrive:
    def __init__(self, creds: Credentials) -> None:
        self.drive_service = build("drive", "v3", credentials=creds)

    def get_all_files(self, mimeType: str) -> list:
        results = (
            self.drive_service.files()
            .list(q=f"mimeType='{mimeType}'", fields="nextPageToken, files(id, name)")
            .execute()
        )
        items = results.get("files", [])
        return items

    def get_all_spreadsheets(self) -> list:
        return self.get_all_files("application/vnd.google-apps.spreadsheet")


if __name__ == "__main__":
    code = input("Enter the auth code: ")
    gdinstance = GoogleDrive(code)
    logger.info(gdinstance.get_all_spreadsheets())

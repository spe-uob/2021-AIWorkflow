from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from loguru import logger

class GoogleDrive:

    def __init__(self, token: str = None) -> None:
        #! BUG: google.auth.exceptions.RefreshError: 
        #! The credentials do not contain the necessary fields need to refresh the access token. 
        #! You must specify refresh_token, token_uri, client_id, and client_secret.
        if token is None: raise ValueError("Token is required")
        creds = Credentials(token)
        self.drive_service = build('drive', 'v3', credentials=creds)
        self.slides_service = build('slides', 'v1', credentials=creds)
        self.sheets_service = build('sheets', 'v4', credentials=creds)

    def get_all_files(self, mimeType: str) -> list:
        results = self.drive_service.files().list(q=f"mimeType='{mimeType}'", fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        return items
    
    def get_all_presentations(self) -> list:
        return self.get_all_files('application/vnd.google-apps.presentation')

    def get_all_spreadsheets(self) -> list:
        return self.get_all_files('application/vnd.google-apps.spreadsheet')

if __name__ == '__main__':
    gdinstance = GoogleDrive("testtoken")
    logger.info(gdinstance.get_all_spreadsheets())
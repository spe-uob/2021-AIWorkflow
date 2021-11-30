from __future__ import print_function
from typing import List
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from loguru import logger
import os.path


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/presentations', 'https://www.googleapis.com/auth/drive']

class GoogleDrive:

    def __init__(self) -> None:
        creds = self.get_credentials()
        self.drive_service = build('drive', 'v3', credentials=creds)
        self.slides_service = build('slides', 'v1', credentials=creds)

    def get_credentials(self) -> Credentials:
        creds = None
        try:
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())
        except Exception as e:
            logger.error(e)
        finally:
            return creds

    def get_all_files(self, mimeType: str) -> list:
        results = self.drive_service.files().list(q=f"mimeType='{mimeType}'", fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        return items
    
    def get_all_presentations(self) -> list:
        return self.get_all_files('application/vnd.google-apps.presentation')

if __name__ == '__main__':
    gdinstance = GoogleDrive()
    logger.info(gdinstance.get_all_presentations())
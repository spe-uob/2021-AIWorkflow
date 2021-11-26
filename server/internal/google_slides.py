from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/presentations.readonly']

# The ID of a sample presentation.
PRESENTATION_ID = '1EAYk18WDjIG-zp_0vLm3CsfQh_i8eXc67Jo2O9C6Vuc'



class GoogleSlides:
    
    def __init__(self, token_filename: str) -> None:
        self.creds = Credentials.from_authorized_user_file(token_filename)


def main():
    """Shows basic usage of the Slides API.
    Prints the number of slides and elments in a sample presentation.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    tokenfile = "gs_token.json"
    if os.path.exists(tokenfile):
        creds = Credentials.from_authorized_user_file(tokenfile, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(tokenfile, 'w') as token:
            token.write(creds.to_json())

    service = build('slides', 'v1', credentials=creds)

    # Call the Slides API
    presentation = service.presentations().get(
        presentationId=PRESENTATION_ID).execute()
    slides = presentation.get('slides')

    print('The presentation contains {} slides:'.format(len(slides)))
    for i, slide in enumerate(slides):
        print('- Slide #{} contains {} elements.'.format(
            i + 1, len(slide.get('pageElements'))))


if __name__ == '__main__':
    main()
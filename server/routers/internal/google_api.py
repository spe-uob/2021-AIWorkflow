from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


class GoogleAPI:
    def __init__(self, creds: str, auth_code: str) -> None:
        flow = Flow.from_client_config(
            creds,
            scopes=[
                "openid",
                "https://www.googleapis.com/auth/userinfo.profile",
                "https://www.googleapis.com/auth/userinfo.email",
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/presentations",
            ],
            redirect_uri="postmessage",
        )
        flow.fetch_token(code=auth_code)
        self._creds = flow.credentials
        self.oauth_service = build("oauth2", "v2", credentials=self._creds)

    @property
    def credentials(self) -> Credentials:
        return self._creds

    def load_profile(self):
        return self.oauth_service.userinfo().get().execute()

from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials


class GoogleAPI:
    def __init__(self, file_path: str, auth_code: str) -> None:
        flow = Flow.from_client_secrets_file(
            file_path,
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

    @property
    def credentials(self) -> Credentials:
        return self._creds

from .google_api import GoogleAPI
from .google_slides import GoogleSlides
from .google_sheets import GoogleSheets

class Users:
    def __init__(self):
        self.__users__ = {}

    def __str__(self):
        text = "Users:\n"
        for user_id in self.__users__:
            text += f"{user_id}:\n"
            for key, value in self.__users__[user_id].items():
                text += f"\t{key}: {value}\n"
        return text
    
    def register_user(self, creds_file: str, auth_code: str): 
        google_api = GoogleAPI(creds_file, auth_code)
        google_creds = google_api.credentials
        user_profile = google_api.load_profile()
        googleslides = GoogleSlides(google_creds)
        googlesheets = GoogleSheets(google_creds)
        backend_authcode = hash(user_profile["id"] + auth_code)
        self.add_user(user_profile["id"], 
            {
                "googleslides": googleslides,
                "googlesheets": googlesheets,
                "auth_code": backend_authcode,
            }
        )
        user_profile.update({"auth_code": backend_authcode})
        return user_profile

    def add_user(self, user_id: str, props: dict):
        self.__users__[user_id] = props

    def remove_user(self, user_id: str):
        self.__users__.pop(user_id)

    def get_users(self):
        return self.__users__
    
    def get_user(self, user_id):
        return self.__users__.get(user_id)

if __name__ == "__main__":
    users = Users()
    users.add_user("1", {"some_props": "some_value"})
    users.add_user("2", {"some_props": "some_value", "some_other_props": "some_other_value"})
    users.add_user("3", {"some_props": "some_value", "some_other_props": "some_other_value"})
    print(users)
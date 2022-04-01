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
    
    def register_user(self, creds_file: str, auth_code: str, user_id: str): 
        google_api = GoogleAPI(creds_file, auth_code)
        google_creds = google_api.credentials
        user_profile = google_api.load_profile()
        googleslides = GoogleSlides(google_creds)
        googlesheets = GoogleSheets(google_creds)
        backend_authcode = hash (user_id + auth_code)
        self.add_user(user_profile["id"], 
            {
                "googleslides": googleslides,
                "googlesheets": googlesheets,
            }
        )
        return user_profile, backend_authcode

    def add_user(self, user_id: str, props: dict):
        self.__users__[user_id] = props

    def remove_user(self, user_id: str):
        self.__users__.pop(user_id)

    def get_users(self):
        return self.__users__
    
    def get_user(self, user_id, auth_code, backend_authcode):
        if (backend_authcode == hash (user_id + auth_code)):
            return self.__users__.get(user_id)
        else:
            print ("invalid auth_code!")

if __name__ == "__main__":
    users = Users()
    users.add_user("1", {"some_props": "some_value"})
    users.add_user("2", {"some_props": "some_value", "some_other_props": "some_other_value"})
    users.add_user("3", {"some_props": "some_value", "some_other_props": "some_other_value"})
    print(users)
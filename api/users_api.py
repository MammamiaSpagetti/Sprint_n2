from api.base_api import BaseApi


class UsersApi(BaseApi):
    def register(self, user_data):
        return self.request("POST", "/signup", json=user_data)

    def login(self, user_data):
        return self.request("POST", "/signin", json=user_data)


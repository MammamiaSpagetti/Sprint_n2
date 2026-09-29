from api.base_api import BaseApi
from urls import LOGIN_USER, REGISTER_USER


class UsersApi(BaseApi):
    def register(self, user_data):
        return self.request("POST", REGISTER_USER, json=user_data)

    def login(self, user_data):
        return self.request("POST", LOGIN_USER, json=user_data)


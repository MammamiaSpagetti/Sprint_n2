from data import DEFAULT_USER_NAME, DUPLICATE_EMAIL_RESPONSE


class TestRegistration:
    def test_register_with_unique_email_returns_user_and_token(self, users_api, user_data):
        response = users_api.register(user_data)

        assert response.status_code == 201
        body = response.json()
        assert isinstance(body["user"]["id"], int)
        assert body["user"]["id"] > 0
        assert body["user"]["email"] == user_data["email"]
        assert body["user"]["name"] == DEFAULT_USER_NAME
        assert isinstance(body["access_token"]["access_token"], str)
        assert body["access_token"]["access_token"]

        login_response = users_api.login(user_data)
        assert login_response.status_code == 201
        assert login_response.json()["user"]["id"] == body["user"]["id"]

    def test_register_with_existing_email_returns_error(self, users_api, registered_user):
        response = users_api.register(registered_user["credentials"])

        assert response.status_code == 400
        assert response.json() == DUPLICATE_EMAIL_RESPONSE


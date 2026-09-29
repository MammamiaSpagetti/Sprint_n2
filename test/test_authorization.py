class TestAuthorization:
    def test_login_registered_user_returns_valid_token(
        self, users_api, listings_api, registered_user
    ):
        response = users_api.login(registered_user["credentials"])

        assert response.status_code == 201
        body = response.json()
        assert body["user"]["id"] == registered_user["user"]["id"]
        assert body["user"]["email"] == registered_user["credentials"]["email"]
        token = body["token"]["access_token"]
        assert isinstance(token, str)
        assert token

        profile_response = listings_api.get_own_listings(token)
        assert profile_response.status_code == 200
        assert profile_response.json()["offers"] == []


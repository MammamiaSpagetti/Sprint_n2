from data import FORBIDDEN_EDIT_RESPONSE, UPDATED_LISTING_NAME


class TestEditListing:
    def test_owner_can_change_listing_name(
        self, listings_api, registered_user, created_listing, listing_data
    ):
        updated_data = {**listing_data, "name": UPDATED_LISTING_NAME}
        token = registered_user["token"]

        response = listings_api.update(created_listing["id"], updated_data, token)

        assert response.status_code == 200
        body = response.json()
        assert body["id"] == created_listing["id"]
        assert body["owner"] == registered_user["user"]["id"]
        assert updated_data.items() <= body.items()

        saved_response = listings_api.get_own_listings(token)
        assert saved_response.status_code == 200
        saved_listings = saved_response.json()["offers"]
        assert len(saved_listings) == 1
        assert saved_listings[0]["id"] == created_listing["id"]
        assert saved_listings[0]["owner"] == registered_user["user"]["id"]
        assert updated_data.items() <= saved_listings[0].items()

    def test_another_user_cannot_edit_listing(
        self, listings_api, registered_user, another_user, created_listing, listing_data
    ):
        updated_data = {**listing_data, "name": UPDATED_LISTING_NAME}
        assert another_user["user"]["id"] != registered_user["user"]["id"]

        response = listings_api.update(
            created_listing["id"], updated_data, another_user["token"]
        )

        assert response.status_code == 401
        assert response.json() == FORBIDDEN_EDIT_RESPONSE

        saved_response = listings_api.get_own_listings(registered_user["token"])
        assert saved_response.status_code == 200
        saved_listings = saved_response.json()["offers"]
        assert len(saved_listings) == 1
        assert saved_listings[0]["id"] == created_listing["id"]
        assert saved_listings[0]["owner"] == registered_user["user"]["id"]
        assert listing_data.items() <= saved_listings[0].items()


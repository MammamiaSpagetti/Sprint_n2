from data import DELETED_LISTING_RESPONSE


class TestDeleteListing:
    def test_owner_can_delete_listing(
        self, listings_api, registered_user, created_listing
    ):
        token = registered_user["token"]

        response = listings_api.delete(created_listing["id"], token)

        assert response.status_code == 200
        assert response.json() == DELETED_LISTING_RESPONSE

        saved_response = listings_api.get_own_listings(token)
        assert saved_response.status_code == 200
        assert saved_response.json()["offers"] == []

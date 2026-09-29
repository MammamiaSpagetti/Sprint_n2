class TestCreateListing:
    def test_create_listing_saves_data_for_current_user(
        self, listings_api, registered_user, listing_data, listing_cleanup
    ):
        token = registered_user["token"]

        response = listings_api.create(listing_data, token)

        assert response.status_code == 201
        listing = response.json()
        listing_cleanup.append((listing["id"], token))
        assert isinstance(listing["id"], int)
        assert listing["id"] > 0
        assert listing_data.items() <= listing.items()
        assert listing["owner"] == registered_user["user"]["id"]

        saved_response = listings_api.get_own_listings(token)
        assert saved_response.status_code == 200
        saved_listings = saved_response.json()["offers"]
        assert len(saved_listings) == 1
        assert saved_listings[0]["id"] == listing["id"]
        assert saved_listings[0]["owner"] == registered_user["user"]["id"]
        assert listing_data.items() <= saved_listings[0].items()


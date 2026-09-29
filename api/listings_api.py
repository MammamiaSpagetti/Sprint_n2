from api.base_api import BaseApi
from urls import CREATE_LISTING, DELETE_LISTING, OWN_LISTINGS, UPDATE_LISTING


class ListingsApi(BaseApi):
    @staticmethod
    def _multipart_fields(listing_data):
        return {name: (None, str(value)) for name, value in listing_data.items()}

    def create(self, listing_data, token):
        return self.request(
            "POST",
            CREATE_LISTING,
            token=token,
            files=self._multipart_fields(listing_data),
        )

    def update(self, listing_id, listing_data, token):
        return self.request(
            "PATCH",
            UPDATE_LISTING.format(listing_id=listing_id),
            token=token,
            files=self._multipart_fields(listing_data),
        )

    def delete(self, listing_id, token):
        return self.request(
            "DELETE", DELETE_LISTING.format(listing_id=listing_id), token=token
        )

    def get_own_listings(self, token, page=1):
        return self.request("GET", OWN_LISTINGS.format(page=page), token=token)


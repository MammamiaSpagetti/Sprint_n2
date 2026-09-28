from api.base_api import BaseApi


class ListingsApi(BaseApi):
    @staticmethod
    def _multipart_fields(listing_data):
        return {name: (None, str(value)) for name, value in listing_data.items()}

    def create(self, listing_data, token):
        return self.request(
            "POST",
            "/create-listing",
            token=token,
            files=self._multipart_fields(listing_data),
        )

    def update(self, listing_id, listing_data, token):
        return self.request(
            "PATCH",
            f"/update-offer/{listing_id}",
            token=token,
            files=self._multipart_fields(listing_data),
        )

    def delete(self, listing_id, token):
        return self.request("DELETE", f"/listings/{listing_id}", token=token)

    def get_own_listings(self, token, page=1):
        return self.request("GET", f"/profile/listings/{page}", token=token)


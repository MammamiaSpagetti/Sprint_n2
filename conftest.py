import pytest
import requests

from api.listings_api import ListingsApi
from api.users_api import UsersApi
from data import LISTING_DATA, PASSWORD
from helpers.email_generator import generate_email


@pytest.fixture
def session():
    with requests.Session() as http_session:
        yield http_session


@pytest.fixture
def users_api(session):
    return UsersApi(session)


@pytest.fixture
def listings_api(session):
    return ListingsApi(session)


@pytest.fixture
def user_data():
    return {"email": generate_email(), "password": PASSWORD}


@pytest.fixture
def user_factory(users_api):
    def create_user(credentials):
        response = users_api.register(credentials)
        response.raise_for_status()
        body = response.json()
        token = body["access_token"]["access_token"]
        return {
            "credentials": credentials,
            "user": body["user"],
            "token": token,
        }

    return create_user


@pytest.fixture
def registered_user(user_factory, user_data):
    return user_factory(user_data)


@pytest.fixture
def another_user(user_factory):
    return user_factory({"email": generate_email(), "password": PASSWORD})


@pytest.fixture
def listing_data():
    return LISTING_DATA.copy()


@pytest.fixture
def listing_cleanup(listings_api):
    created_listings = []
    yield created_listings
    for listing_id, token in reversed(created_listings):
        response = listings_api.get_own_listings(token)
        response.raise_for_status()
        own_ids = {listing["id"] for listing in response.json()["offers"]}
        if listing_id in own_ids:
            deleted = listings_api.delete(listing_id, token)
            deleted.raise_for_status()


@pytest.fixture
def created_listing(listings_api, registered_user, listing_data, listing_cleanup):
    token = registered_user["token"]
    response = listings_api.create(listing_data, token)
    response.raise_for_status()
    listing = response.json()
    listing_cleanup.append((listing["id"], token))
    return listing


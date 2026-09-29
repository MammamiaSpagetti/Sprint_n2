from config import BASE_URL, REQUEST_TIMEOUT


class BaseApi:
    def __init__(self, session):
        self.session = session

    def request(self, method, endpoint, token=None, **kwargs):
        headers = {}
        if token is not None:
            headers["Authorization"] = f"Bearer {token}"
        return self.session.request(
            method,
            f"{BASE_URL}{endpoint}",
            headers=headers,
            timeout=REQUEST_TIMEOUT,
            **kwargs,
        )


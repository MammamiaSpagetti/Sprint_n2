import os


BASE_URL = os.getenv(
    "DESK_API_URL", "https://qa-desk.education-services.ru/api"
).rstrip("/")
REQUEST_TIMEOUT = 30


EMAIL_DOMAIN = "example.com"
PASSWORD = "Sprint2_Test_2026!"
DEFAULT_USER_NAME = "User"

LISTING_DATA = {
    "name": "Тестовая книга по Python",
    "category": "Книги",
    "condition": "Новый",
    "city": "Москва",
    "description": "Тестовое объявление для проверки API учебного сервиса.",
    "price": 1500,
}
UPDATED_LISTING_NAME = "Обновлённая тестовая книга по Python"

DUPLICATE_EMAIL_RESPONSE = {
    "statusCode": 400,
    "message": "Почта уже используется",
}
FORBIDDEN_EDIT_RESPONSE = {
    "message": "Оффер не найден или у вас нет прав на его редактирование",
    "error": "Unauthorized",
    "statusCode": 401,
}
DELETED_LISTING_RESPONSE = {"message": "Объявление удалено успешно"}


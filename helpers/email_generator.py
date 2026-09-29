from uuid import uuid4

from data import EMAIL_DOMAIN


def generate_email():
    """Возвращает новый email для каждого вызова, в том числе при параллельном запуске."""
    return f"sprint2_{uuid4().hex}@{EMAIL_DOMAIN}"


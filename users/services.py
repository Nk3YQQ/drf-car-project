from django.contrib.auth.hashers import make_password

from users.models import User


def create_user():
    """Функция для создания пользователя"""

    return User.objects.create(
        first_name="Test",
        last_name="Testov",
        email="test.testov@mail.ru",
        password=make_password("123qwe456rty"),
        is_active=True,
    )


def create_other_user():
    """Функция для создания другого пользователя"""

    return User.objects.create(
        first_name="Ivan",
        last_name="Ivanov",
        email="ivan.ivanov@mail.ru",
        password=make_password("123qwe456rty"),
        is_active=True,
    )

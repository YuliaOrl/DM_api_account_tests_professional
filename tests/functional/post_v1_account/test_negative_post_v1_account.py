import pytest
import allure
from collections import namedtuple
from datetime import datetime
from checkers.http_checkers import check_status_code_http
from clients.http.dm_api_account.models.registration import Registration


def new_user():
    now = datetime.now()
    time = now.strftime("%H_%M_%S_%f")
    login = f"Testov_{time}"
    password = "123456789"
    email = f"{login}@yandex.ru"
    User = namedtuple("User", ["login", "password", "email"])
    user = User(login=login, password=password, email=email)
    return user


@allure.epic("DM.API Account")
@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты на проверку метода POST v1/account")
@allure.sub_suite("Негативные тесты")
class TestsNegativePostV1Account:
    user = new_user()

    @allure.title("Негативная проверка регистрации нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "error_message, registration",
        [
            [
                {"Password": ["Short"]},
                Registration(login=user.login, email=user.email, password=user.password[:5]),
            ],
            [
                {"Email": ["Invalid"]},
                Registration(
                    login=user.login,
                    email=user.email.replace("@", ""),
                    password=user.password,
                ),
            ],
            [
                {"Login": ["Short"]},
                Registration(login=user.login[0], email=user.email, password=user.password),
            ],
        ],
    )
    async def test_negative_post_v1_account(self, account_helper, error_message, registration):
        allure.dynamic.description(
            f"Тест проверяет ожидаемый статус код 400 и сообщение об ошибке {error_message} "
            f"от сервера при регистрации нового пользователя, если использовать "
            f"невалидный {next(iter(error_message)).lower()}."
        )
        with check_status_code_http(
            expected_status_code=400,
            expected_title_message="Validation failed",
            expected_error_message=error_message,
        ):
            await account_helper.dm_account_api.account_api.post_v1_account(registration=registration)

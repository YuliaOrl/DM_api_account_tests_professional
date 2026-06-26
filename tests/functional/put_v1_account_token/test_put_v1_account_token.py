import allure
from clients.http.dm_api_account.models.user import User
from helpers.account_helper import AccountHelper


@allure.epic("DM.API Account")
@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты на проверку метода PUT v1/account/token")
@allure.sub_suite("Позитивные тесты")
class TestPutV1AccountToken:
    @allure.title("Проверка активации пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Тест проверяет создание нового пользователя, его успешную активацию и последующую авторизацию."
    )
    async def test_put_v1_account_token(self, account_helper: AccountHelper, prepare_user: User) -> None:
        login, password, email = (
            prepare_user.login,
            prepare_user.password,
            prepare_user.email,
        )

        await account_helper.register_new_user(login=login, password=password, email=email)
        await account_helper.user_login(login=login, password=password)

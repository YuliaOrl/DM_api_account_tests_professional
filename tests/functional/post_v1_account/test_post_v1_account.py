import allure
from checkers.post_v1_account import PostV1Account
from clients.http.dm_api_account.models.user import User
from clients.http.dm_api_account.models.user_envelope import UserEnvelope
from helpers.account_helper import AccountHelper


@allure.epic("DM.API Account")
@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты на проверку метода POST v1/account")
@allure.sub_suite("Позитивные тесты")
class TestsPostV1Account:
    @allure.title("Проверка регистрации нового пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Тест проверяет успешную регистрацию нового пользователя с его последующей авторизацией и проверкой содержания ответа."
    )
    async def test_post_v1_account(self, account_helper: AccountHelper, prepare_user: User) -> None:
        login, password, email = (
            prepare_user.login,
            prepare_user.password,
            prepare_user.email,
        )

        await account_helper.register_new_user(login=login, password=password, email=email)
        response = await account_helper.user_login(login=login, password=password, validate_response=True)
        if isinstance(response, UserEnvelope):
            PostV1Account.check_response_values(login, response)
        else:
            raise AssertionError("Ожидался UserEnvelope, получен httpx.Response")

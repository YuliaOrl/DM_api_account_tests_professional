import allure
from checkers.get_v1_account import GetV1Account
from checkers.http_checkers import check_status_code_http
from clients.http.dm_api_account.models.user import User
from helpers.account_helper import AccountHelper


@allure.epic("DM.API Account")
@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты на проверку метода GET v1/account")
@allure.sub_suite("Позитивные тесты")
class TestsGetV1Account:
    @allure.title("Проверка получения информации о пользователе")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Тест выполняет успешное получение информации об авторизованном пользователе с проверкой содержания ответа."
    )
    async def test_get_v1_account_auth(self, auth_account_helper: AccountHelper, prepare_user: User) -> None:
        with check_status_code_http():
            response = await auth_account_helper.get_current_user()
            GetV1Account.check_response_values(response, prepare_user)

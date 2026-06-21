import allure
from helpers.account_helper import AccountHelper


@allure.epic("DM.API Account")
@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты на проверку метода Delete v1/account/login/all")
@allure.sub_suite("Позитивные тесты")
class TestsDeleteV1AccountLoginAll:
    @allure.title("Проверка выхода авторизованного пользователя из аккаунта на всех устройствах")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Тест проверяет успешный выход пользователя из аккаунта на всех устройствах.")
    async def test_delete_v1_account_login_all(self, auth_account_helper: AccountHelper) -> None:
        await auth_account_helper.user_logout_all()

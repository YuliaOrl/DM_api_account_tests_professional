import allure


@allure.epic("DM.API Account")
@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты на проверку метода Delete v1/account/login")
@allure.sub_suite("Позитивные тесты")
class TestsDeleteV1AccountLogin:
    @allure.title("Проверка выхода авторизованного пользователя из аккаунта")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Тест проверяет успешный выход пользователя из аккаунта.")
    async def test_delete_v1_account_login(self, auth_account_helper):
        await auth_account_helper.user_logout()

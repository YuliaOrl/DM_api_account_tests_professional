import allure


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
    async def test_put_v1_account_token(self, account_helper, prepare_user):
        login, password, email = (
            prepare_user.login,
            prepare_user.password,
            prepare_user.email,
        )

        await account_helper.register_new_user(
            login=login, password=password, email=email
        )
        await account_helper.user_login(login=login, password=password)

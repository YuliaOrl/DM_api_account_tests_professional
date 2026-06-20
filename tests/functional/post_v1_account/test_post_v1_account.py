import allure
from checkers.post_v1_account import PostV1Account


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
    async def test_post_v1_account(self, account_helper, prepare_user):
        login, password, email = (
            prepare_user.login,
            prepare_user.password,
            prepare_user.email,
        )

        await account_helper.register_new_user(
            login=login, password=password, email=email
        )
        response = await account_helper.user_login(
            login=login, password=password, validate_response=True
        )
        PostV1Account.check_response_values(login, response)

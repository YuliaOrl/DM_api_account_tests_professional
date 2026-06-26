import allure


@allure.epic("DM.API Account")
@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты на проверку метода POST v1/account/login")
@allure.sub_suite("Позитивные тесты")
class TestPostV1AccountLogin:
    @allure.title("Проверка авторизации пользователя")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Тест проверяет успешную регистрацию нового пользователя и его последующую авторизацию.")
    async def test_post_v1_account_login(self, account_helper, prepare_user):
        login, password, email = (
            prepare_user.login,
            prepare_user.password,
            prepare_user.email,
        )

        await account_helper.register_new_user(login=login, password=password, email=email)
        await account_helper.user_login(login=login, password=password)

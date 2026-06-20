import allure


@allure.epic("DM.API Account")
@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты на проверку метода PUT v1/account/password")
@allure.sub_suite("Позитивные тесты")
class TestPutV1AccountPassword:
    @allure.title("Проверка изменения пароля пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Тест проверяет успешную смену пароля пользователя с последующей авторизацией с новым паролем."
    )
    async def test_put_v1_account_password(self, account_helper, prepare_user):
        login, password, email = (
            prepare_user.login,
            prepare_user.password,
            prepare_user.email,
        )
        new_password = password[::-1]

        await account_helper.register_new_user(
            login=login, password=password, email=email
        )
        await account_helper.auth_client(login=login, password=password)
        await account_helper.change_password(
            login=login, password=password, email=email, new_password=new_password
        )
        await account_helper.user_login(login=login, password=new_password)

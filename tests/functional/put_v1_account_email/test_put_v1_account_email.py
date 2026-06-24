import allure
from checkers.http_checkers import check_status_code_http


@allure.epic("DM.API Account")
@allure.parent_suite("Функциональные тесты")
@allure.suite("Тесты на проверку метода PUT v1/account/email")
@allure.sub_suite("Позитивные тесты")
class TestPutV1AccountEmail:
    @allure.title("Проверка изменения емейла пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Тест проверяет создание пользователя, изменение его емейла, авторизацию без активации смены "
        "пароля и получение ошибки 403, последующую активацию пользователя и его успешную авторизацию."
    )
    async def test_put_v1_account_email(self, account_helper, prepare_user):
        login, password, email = (
            prepare_user.login,
            prepare_user.password,
            prepare_user.email,
        )
        new_email = email.replace("@", "_new_email@")

        await account_helper.register_new_user(login=login, password=password, email=email)
        await account_helper.user_login(login=login, password=password)
        await account_helper.change_email(login=login, password=password, new_email=new_email)
        with check_status_code_http(403, "User is inactive. Address the technical support for more details"):
            await account_helper.user_login(login=login, password=password)
        await account_helper.user_activation(login=login)
        await account_helper.user_login(login=login, password=password)

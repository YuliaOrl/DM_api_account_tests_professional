import asyncio
import allure
from checkers.http_checkers import check_status_code_http


@allure.epic('DM.API Account')
@allure.parent_suite('Функциональные тесты')
@allure.suite('Тесты на проверку метода GET v1/account')
@allure.sub_suite('Негативные тесты')
class TestsNegativeGetV1Account:

    @allure.title('Негативная проверка получения информации о неавторизованном пользователе')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Тест проверяет получение ожидаемого статус кода 401 и сообщения об ошибке '
                        '"User must be authenticated" от сервера при попытке запроса информации о пользователе, '
                        'если пользователь не авторизован.')
    async def test_get_v1_account_no_auth(self, account_helper):
        with check_status_code_http(401, 'User must be authenticated'):
            await account_helper.get_current_user()


    @allure.title('Негативная проверка получения информации о неавторизованном пользователе при ddos-запросах')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Тест проверяет получение ожидаемого статус кода 401 и сообщения об ошибке '
                        '"User must be authenticated" от сервера при попытке запроса информации о пользователе, '
                        'если пользователь не авторизован.')
    async def test_get_v1_account_no_auth_ddos(self, account_helper):
        with check_status_code_http(401, 'User must be authenticated'):
            ddos_tasks = []
            for _ in range(50):
                ddos_tasks.append(account_helper.get_current_user())
            await asyncio.gather(*ddos_tasks)
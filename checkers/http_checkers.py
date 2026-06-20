import allure
import requests
import httpx
from contextlib import contextmanager


@contextmanager
def check_status_code_http(
    expected_status_code: int = requests.codes.OK,
    expected_title_message: str = None,
    expected_error_message: str = None,
):
    with allure.step(f"Проверка ожидаемого статус кода ответа: {expected_status_code}"):
        try:
            yield
            if expected_status_code != requests.codes.OK:
                raise AssertionError(
                    f"Ожидаемый статус код должен быть равен {expected_status_code}"
                )
            if expected_title_message:
                raise AssertionError(
                    f'Должно быть получено сообщение "{expected_title_message}", но запрос прошёл успешно'
                )
        except httpx.HTTPStatusError as e:
            assert e.response.status_code == expected_status_code
            assert e.response.json().get("title") == expected_title_message
            assert e.response.json().get("errors") == expected_error_message

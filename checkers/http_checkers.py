import allure
import httpx
from json import loads
from typing import Iterator
from contextlib import contextmanager
from dm_api_account.exceptions import ApiException


@contextmanager
def check_status_code_http(
    expected_status_code: int = httpx.codes.OK,
    expected_title_message: str | None = None,
    expected_error_message: dict[str, list[str]] | None = None,
) -> Iterator[None]:
    with allure.step(f"Проверка ожидаемого статус кода ответа: {expected_status_code}"):
        try:
            yield
            if expected_status_code != httpx.codes.OK:
                raise AssertionError(f"Ожидаемый статус код должен быть равен {expected_status_code}")
            if expected_title_message:
                raise AssertionError(
                    f'Должно быть получено сообщение "{expected_title_message}", но запрос прошёл успешно'
                )
        except httpx.HTTPStatusError as e:
            assert e.response.status_code == expected_status_code
            assert e.response.json().get("title") == expected_title_message
            assert e.response.json().get("errors") == expected_error_message
        except ApiException as e:  # Обработка исключений OpenAPI-клиента, которые наследуются от ApiException
            assert e.status == expected_status_code, f"Ожидался статус код {expected_status_code}, получен {e.status}"
            if e.body:
                response_json = loads(e.body)
                if expected_title_message:
                    assert response_json.get("title") == expected_title_message, (
                        f"Ожидалось сообщение '{expected_title_message}', получено '{response_json.get('title')}'"
                    )
                if expected_error_message:
                    assert response_json.get("errors") == expected_error_message, (
                        f"Ожидались ошибки {expected_error_message}, получены {response_json.get('errors')}"
                    )

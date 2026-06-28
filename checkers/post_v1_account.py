import allure
from datetime import datetime, timezone
from hamcrest import assert_that, starts_with, equal_to, instance_of, has_property, has_properties
from clients.http.dm_api_account.models.api_models import UserEnvelope


class PostV1Account:
    @classmethod
    def check_response_values(cls, login: str, response: UserEnvelope) -> None:
        with allure.step("Проверка ответа"):
            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            assert_that(str(response.resource.registration), starts_with(today))
            assert_that(
                response,
                has_property(
                    "resource",
                    has_properties(
                        {
                            "login": starts_with(login[: login.find("_")]),
                            "registration": instance_of(datetime),
                            "rating": has_properties(
                                {
                                    "enabled": equal_to(True),
                                    "quality": equal_to(0),
                                    "quantity": equal_to(0),
                                }
                            ),
                        }
                    ),
                ),
            )

import allure
from datetime import datetime, timezone
from hamcrest import (
    assert_that,
    starts_with,
    all_of,
    has_property,
    has_properties,
    equal_to,
    instance_of,
)


class PostV1Account:
    @classmethod
    def check_response_values(cls, login, response):
        with allure.step("Проверка ответа"):
            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            assert_that(str(response.resource.registration), starts_with(today))
            assert_that(
                response,
                all_of(
                    has_property(
                        "resource",
                        has_property("login", starts_with(login[: login.find("_")])),
                    ),
                    has_property(
                        "resource", has_property("registration", instance_of(datetime))
                    ),
                    has_property(
                        "resource",
                        has_property(
                            "rating",
                            has_properties(
                                {
                                    "enabled": equal_to(True),
                                    "quality": equal_to(0),
                                    "quantity": equal_to(0),
                                }
                            ),
                        ),
                    ),
                ),
            )

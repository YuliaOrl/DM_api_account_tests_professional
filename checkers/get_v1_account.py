import allure
from datetime import datetime, timezone
from hamcrest import (
    assert_that,
    has_property,
    has_properties,
    anything,
    is_in,
    equal_to,
    only_contains,
    all_of,
    instance_of,
)


class GetV1Account:
    @classmethod
    def check_response_values(cls, response, prepare_user):
        with allure.step("Проверка ответа"):
            assert_that(
                response,
                has_property(
                    "resource",
                    has_properties(
                        {
                            "info": anything(),
                            "settings": has_properties(
                                {
                                    "color_schema": is_in(
                                        [
                                            "Modern",
                                            "Pale",
                                            "Classic",
                                            "ClassicPale",
                                            "Night",
                                        ]
                                    ),
                                    "paging": has_properties(
                                        {
                                            "posts_per_page": equal_to(10),
                                            "comments_per_page": equal_to(10),
                                            "topics_per_page": equal_to(10),
                                            "messages_per_page": equal_to(10),
                                            "entities_per_page": equal_to(10),
                                        }
                                    ),
                                }
                            ),
                            "login": equal_to(prepare_user.login),
                            "roles": only_contains(
                                "Guest",
                                "Player",
                                "Administrator",
                                "NannyModerator",
                                "RegularModerator",
                                "SeniorModerator",
                            ),
                            "rating": has_properties(
                                {
                                    "enabled": equal_to(True),
                                    "quality": equal_to(0),
                                    "quantity": equal_to(0),
                                }
                            ),
                            "online": all_of(
                                instance_of(datetime),
                                has_properties(
                                    {
                                        "month": equal_to(datetime.now(timezone.utc).month),
                                        "day": equal_to(datetime.now(timezone.utc).day),
                                        "hour": equal_to(datetime.now(timezone.utc).hour),
                                    }
                                ),
                            ),
                            "registration": all_of(
                                instance_of(datetime),
                                has_properties(
                                    {
                                        "year": equal_to(datetime.now(timezone.utc).year),
                                        "month": equal_to(datetime.now(timezone.utc).month),
                                        "day": equal_to(datetime.now(timezone.utc).day),
                                    }
                                ),
                            ),
                        }
                    ),
                ),
            )

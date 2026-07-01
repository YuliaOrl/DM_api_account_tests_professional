import allure
import httpx
from datetime import datetime, timezone
from clients.http.dm_api_account.models.user import User
from clients.http.dm_api_account.models.api_models import UserDetailsEnvelope, ColorSchema, UserRole
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
    any_of,
    none,
)


class GetV1Account:
    @classmethod
    def check_response_values(cls, response: UserDetailsEnvelope | httpx.Response, prepare_user: User) -> None:
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
                                            ColorSchema.MODERN.value,
                                            ColorSchema.PALE.value,
                                            ColorSchema.CLASSIC.value,
                                            ColorSchema.CLASSIC_PALE.value,
                                            ColorSchema.NIGHT.value,
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
                                UserRole.GUEST.value,
                                UserRole.PLAYER.value,
                                UserRole.ADMINISTRATOR.value,
                                UserRole.NANNY_MODERATOR.value,
                                UserRole.REGULAR_MODERATOR.value,
                                UserRole.SENIOR_MODERATOR.value,
                            ),
                            "rating": has_properties(
                                {
                                    "enabled": equal_to(True),
                                    "quality": equal_to(0),
                                    "quantity": equal_to(0),
                                }
                            ),
                            "online": any_of(
                                none(),  # type: ignore[arg-type]
                                all_of(  # type: ignore[arg-type]
                                    instance_of(datetime),
                                    has_properties(
                                        {
                                            "month": equal_to(datetime.now(timezone.utc).month),
                                            "day": equal_to(datetime.now(timezone.utc).day),
                                            "hour": equal_to(datetime.now(timezone.utc).hour),
                                        }
                                    ),
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

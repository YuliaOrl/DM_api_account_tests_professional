import asyncio
import allure
import httpx
from typing import Any, Callable
from json import loads
from dm_api_account.models import (
    ChangeEmail,
    ChangePassword,
    LoginCredentials,
    Registration,
    ResetPassword,
    UserDetailsEnvelope,
    UserEnvelope,
)
from clients.http.dm_api_account.models.user import User
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi


def retrier(function: Callable) -> Callable:
    async def wrapper(*args: Any, **kwargs: Any) -> None:
        token = None
        cnt = 1
        while token is None:
            print(f"Попытка получения токена номер {cnt}!")
            try:
                token = await function(*args, **kwargs)
            except Exception as e:
                print(f"Ошибка при выполнении функции: {e}")
                token = None
            cnt += 1
            if cnt == 6:
                raise AssertionError("Превышено количество попыток получения токена активации!")
            if token:
                return token
            await asyncio.sleep(1)

    return wrapper


class AccountHelper:
    def __init__(self, dm_account_api: DMApiAccount, mailhog: MailHogApi):
        self.dm_account_api = dm_account_api
        self.mailhog = mailhog
        self.token: str = ""

    @allure.step("Авторизация нового пользователя")
    async def auth_client(self, login: str, password: str) -> None:
        login_credentials = LoginCredentials(login=login, password=password, rememberMe=True)
        response = await self.dm_account_api.login_api.v1_account_login_post_with_http_info(
            login_credentials=login_credentials
        )
        token = response.headers.get("X-Dm-Auth-Token")
        if token:
            self.token = token
            self.dm_account_api.api_client.default_headers.update({"X-Dm-Auth-Token": token})

    @allure.step("Регистрация нового пользователя")
    async def register_new_user(self, login: str, password: str, email: str) -> User:
        user = User(login=login, password=password, email=email)
        registration = Registration(login=login, email=email, password=password)
        await self.dm_account_api.account_api.register(registration=registration)
        # assert response.status_code == 201, f"Пользователь не был создан {response.json()}"
        await self.user_activation(login=login)
        return user

    @allure.step("Авторизация пользователя")
    async def user_login(
        self,
        login: str,
        password: str,
        remember_me: bool = True,
        validate_response: bool = True,
        validate_headers: bool = False,
    ) -> UserEnvelope | httpx.Response:
        login_credentials = LoginCredentials(login=login, password=password, rememberMe=remember_me)
        if validate_response:
            return await self.dm_account_api.login_api.v1_account_login_post(login_credentials=login_credentials)

        response = await self.dm_account_api.login_api.v1_account_login_post_with_http_info(
            login_credentials=login_credentials
        )
        response.raise_for_status()
        if validate_headers:
            assert response.headers.get("x-dm-auth-token"), f"Токен для пользователя {login} не был получен"
        return response

    @allure.step("Получение информации о текущем пользователе")
    async def get_current_user(self, validate_response: bool = True) -> UserDetailsEnvelope | httpx.Response:
        if validate_response:
            return await self.dm_account_api.account_api.get_current(x_dm_auth_token=self.token)

        response = await self.dm_account_api.account_api.get_current_with_http_info(x_dm_auth_token=self.token)
        response.raise_for_status()
        return response

    @allure.step("Изменение емейла")
    async def change_email(self, login: str, password: str, new_email: str) -> UserEnvelope | httpx.Response:
        change_email = ChangeEmail(login=login, password=password, email=new_email)
        response = await self.dm_account_api.account_api.change_email_with_http_info(change_email=change_email)
        return response

    @allure.step("Изменение пароля")
    async def change_password(
        self, login: str, password: str, email: str, new_password: str
    ) -> UserEnvelope | httpx.Response:
        reset_password = ResetPassword(login=login, email=email)
        await self.dm_account_api.account_api.reset_password_with_http_info(reset_password=reset_password)
        token = await self.get_activation_token_by_login(login, confirm="password")
        assert token is not None, f"Токен для пользователя {login} не был получен"
        change_password = ChangePassword(login=login, token=token, oldPassword=password, newPassword=new_password)
        response = await self.dm_account_api.account_api.change_password_with_http_info(change_password=change_password)
        return response

    @allure.step("Активация пользователя")
    async def user_activation(self, login: str) -> UserEnvelope | httpx.Response:
        token = await self.get_activation_token_by_login(login)
        assert token is not None, f"Токен для пользователя {login} не был получен"
        response = await self.dm_account_api.account_api.activate(token=token)
        return response

    @allure.step("Выход пользователя из аккаунта")
    async def user_logout(self) -> httpx.Response:
        response = await self.dm_account_api.login_api.v1_account_login_delete_with_http_info(
            x_dm_auth_token=self.token
        )
        assert response.status_code == 204, "Выход из аккаунта не был выполнен"
        return response

    @allure.step("Выход пользователя из аккаунта на всех устройствах")
    async def user_logout_all(self) -> httpx.Response:
        response = await self.dm_account_api.login_api.v1_account_login_all_delete_with_http_info(
            x_dm_auth_token=self.token
        )
        assert response.status_code == 204, "Выход из аккаунта на всех устройствах не был выполнен"
        return response

    @allure.step("Получение активационного токена по логину")
    @retrier
    async def get_activation_token_by_login(self, login: str, confirm: str = "activate") -> str | None:
        conf_token = {
            "activate": "ConfirmationLinkUrl",
            "password": "ConfirmationLinkUri",
        }
        response = await self.mailhog.mailhog_api.get_api_v2_messages()
        for item in response.json().get("items", []):
            user_data = loads(item.get("Content", {}).get("Body"))
            if user_data.get("Login") == login:
                token = user_data.get(conf_token[confirm], "").split("/")[-1]
                if token:
                    print(f"Login: {login}, token: {token}")
                    return token
        return None

import time
import allure
from json import loads
from clients.http.dm_api_account.models.change_email import ChangeEmail
from clients.http.dm_api_account.models.change_password import ChangePassword
from clients.http.dm_api_account.models.login_credentials import LoginCredentials
from clients.http.dm_api_account.models.registration import Registration
from clients.http.dm_api_account.models.reset_password import ResetPassword
from clients.http.dm_api_account.models.user import User
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi


def retrier(function):
    async def wrapper(*args, **kwargs):
        token = None
        cnt = 1
        while token is None:
            print(f"Попытка получения токена номер {cnt}!")
            token = await function(*args, **kwargs)
            cnt += 1
            if cnt == 6:
                raise AssertionError("Превышено количество попыток получения токена активации!")
            if token:
                return token
            time.sleep(1)

    return wrapper


class AccountHelper:
    def __init__(self, dm_account_api: DMApiAccount, mailhog: MailHogApi):
        self.dm_account_api = dm_account_api
        self.mailhog = mailhog

    @allure.step("Авторизация нового пользователя")
    async def auth_client(self, login: str, password: str, validate_response=False):
        login_credentials = LoginCredentials(login=login, password=password, remember_me=True)
        response = await self.dm_account_api.login_api.post_v1_account_login(
            login_credentials=login_credentials, validate_response=validate_response
        )
        token = {"x-dm-auth-token": response.headers["x-dm-auth-token"]}
        self.dm_account_api.account_api.set_headers(token)
        self.dm_account_api.login_api.set_headers(token)

    @allure.step("Регистрация нового пользователя")
    async def register_new_user(self, login: str, password: str, email: str):
        user = User(login=login, password=password, email=email)
        registration = Registration(login=login, email=email, password=password)
        response = await self.dm_account_api.account_api.post_v1_account(registration=registration)
        assert response.status_code == 201, f"Пользователь не был создан {response.json()}"
        await self.user_activation(login=login)
        return user

    @allure.step("Авторизация пользователя")
    async def user_login(
        self,
        login: str,
        password: str,
        remember_me: bool = True,
        validate_response=True,
        validate_headers=False,
    ):
        login_credentials = LoginCredentials(login=login, password=password, remember_me=remember_me)
        response = await self.dm_account_api.login_api.post_v1_account_login(
            login_credentials=login_credentials, validate_response=validate_response
        )
        if validate_headers and not validate_response:
            assert response.headers["x-dm-auth-token"], f"Токен для пользователя {login} не был получен"
        return response

    @allure.step("Получение информации о текущем пользователе")
    async def get_current_user(self):
        response = await self.dm_account_api.account_api.get_v1_account()
        return response

    @allure.step("Изменение емейла")
    async def change_email(self, login: str, password: str, new_email: str):
        change_email = ChangeEmail(login=login, password=password, email=new_email)
        response = await self.dm_account_api.account_api.put_v1_account_email(change_email=change_email)
        return response

    @allure.step("Изменение пароля")
    async def change_password(self, login: str, password: str, email: str, new_password: str):
        reset_password = ResetPassword(login=login, email=email)
        await self.dm_account_api.account_api.post_v1_account_password(reset_password=reset_password)
        token = await self.get_activation_token_by_login(login, confirm="password")
        assert token is not None, f"Токен для пользователя {login} не был получен"
        change_password = ChangePassword(login=login, token=token, old_password=password, new_password=new_password)
        response = await self.dm_account_api.account_api.put_v1_account_password(change_password=change_password)
        return response

    @allure.step("Активация пользователя")
    async def user_activation(self, login: str):
        token = await self.get_activation_token_by_login(login)
        assert token is not None, f"Токен для пользователя {login} не был получен"
        response = await self.dm_account_api.account_api.put_v1_account_token(token=token)
        return response

    @allure.step("Выход пользователя из аккаунта")
    async def user_logout(self):
        response = await self.dm_account_api.login_api.delete_v1_account_login()
        assert response.status_code == 204, "Выход из аккаунта не был выполнен"
        return response

    @allure.step("Выход пользователя из аккаунта на всех устройствах")
    async def user_logout_all(self):
        response = await self.dm_account_api.login_api.delete_v1_account_login_all()
        assert response.status_code == 204, "Выход из аккаунта на всех устройствах не был выполнен"
        return response

    @allure.step("Получение активационного токена по логину")
    @retrier
    async def get_activation_token_by_login(self, login, confirm="activate"):
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

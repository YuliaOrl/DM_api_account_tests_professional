import httpx
from typing import Optional
from clients.http.dm_api_account.apis.account_api import AccountApi
from clients.http.dm_api_account.apis.login_api import LoginApi


class DMApiAccount:
    def __init__(self, host: str, headers: Optional[dict] = None, disable_log: bool = True):
        self.api_client = httpx.AsyncClient(base_url=host, headers=headers)
        self.account_api = AccountApi(api_client=self.api_client)
        self.login_api = LoginApi(api_client=self.api_client)

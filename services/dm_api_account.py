from dm_api_account.api_client import ApiClient
from dm_api_account.configuration import Configuration
from dm_api_account.api.account_api import AccountApi
from dm_api_account.api.login_api import LoginApi


class DMApiAccount:
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.api_client = ApiClient(configuration=self.configuration)
        self.account_api = AccountApi(api_client=self.api_client)
        self.login_api = LoginApi(api_client=self.api_client)

from clients.http.api_mailhog.apis.mailhog_api import MailhogApi
from dm_api_account.configuration import Configuration


class MailHogApi:
    def __init__(self, configuration: Configuration):
        self.configuration = configuration
        self.mailhog_api = MailhogApi(base_url=self.configuration.host)

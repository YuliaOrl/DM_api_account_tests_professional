from typing import Optional
from clients.http.api_mailhog.apis.mailhog_api import MailhogApi


class MailHogApi:
    def __init__(self, host: str, headers: Optional[dict] = None, disable_log: bool = True):
        self.mailhog_api = MailhogApi(base_url=host)

import allure
import httpx
from restclient.client import RestClient


class MailhogApi(RestClient):
    @allure.step("Получение писем из почтового сервера")
    async def get_api_v2_messages(self, limit: int = 50) -> httpx.Response:
        """
        Get Users emails
        :return:
        """
        params = {
            "limit": limit,
        }
        response = await self.get(path="/api/v2/messages", params=params)
        return response

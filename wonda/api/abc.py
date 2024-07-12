from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wonda.api import Token
    from wonda.net import ABCNetworkClient


class ABCAPI(ABC):
    API_URL = "https://api.telegram.org/"

    network_client: "ABCNetworkClient"
    token: "Token"

    @property
    def api_url(self) -> str:
        """
        URL for API requests.
        """
        return self.API_URL + f"bot{self.token}/"

    @property
    def file_url(self) -> str:
        """
        Link to the file storage of the bot.
        """
        return self.API_URL + f"file/bot{self.token}/"

    @abstractmethod
    async def request(self, method: str, params: dict) -> bytes:
        """
        Makes a single request to the API.
        """

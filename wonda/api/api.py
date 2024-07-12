from wonda.api.abc import ABCAPI
from wonda.api.utils import Token
from wonda.errors.external import APIException
from wonda.modules import logger
from wonda.net.abc import ABCNetworkClient
from wonda.net.default import DefaultNetworkClient
from wonda.types.helper import Response, from_json, translate
from wonda.types.methods import APIMethods


class DefaultAPI(ABCAPI, APIMethods):
    REQUEST_URL = "https://api.telegram.org/"

    def __init__(
        self, token: Token, *, http_client: ABCNetworkClient | None = None
    ) -> None:
        super().__init__(self)

        self.token = token
        self.network_client = http_client or DefaultNetworkClient()

    async def request(self, method: str, params: dict) -> bytes:
        await logger.adebug("Calling", method=method, params=params)

        data = self.network_client.construct_form(
            {k: translate(v) for k, v in params.items()}
        )
        response = await self.network_client.request_bytes(
            self.api_url + method, data=data
        )
        result = from_json(response, type=Response)

        if not result.ok:
            raise APIException[result.error_code](result.description, result.error_code)

        await logger.adebug("Received", result=result)
        return result.result

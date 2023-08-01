from wonda.api.abc import ABCAPI
from wonda.api.utils import Token
from wonda.api.validators import (
    DEFAULT_REQUEST_VALIDATORS,
    DEFAULT_RESPONSE_VALIDATORS,
    ABCRequestValidator,
    ABCResponseValidator,
)
from wonda.modules import logger
from wonda.net.abc import ABCNetworkClient
from wonda.net.default import DefaultNetworkClient
from wonda.types.methods import APIMethods


class API(ABCAPI, APIMethods):
    def __init__(
        self, token: Token, http_client: ABCNetworkClient | None = None
    ) -> None:
        super().__init__(self)

        self.token = token
        self.http_client = http_client or DefaultNetworkClient()
        self.request_validators: list[ABCRequestValidator] = DEFAULT_REQUEST_VALIDATORS
        self.response_validators: list[
            ABCResponseValidator
        ] = DEFAULT_RESPONSE_VALIDATORS

    async def request(self, method: str, params: dict = {}) -> bytes | None:
        await logger.debug("Calling", method=method, params=params)

        data = await self.validate_request(params or {})
        response = await self.http_client.request_bytes(
            self.api_url + method, data=data
        )

        await logger.debug("Received", response=response)
        return await self.validate_response(response)

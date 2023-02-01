from typing import List, Optional

from wonda.api.abc import ABCAPI, APIResponse
from wonda.api.utils import Token
from wonda.api.validators import (
    DEFAULT_REQUEST_VALIDATORS,
    DEFAULT_RESPONSE_VALIDATORS,
    ABCRequestValidator,
    ABCResponseValidator,
)
from wonda.http.abc import ABCHTTPClient
from wonda.http.aiohttp import AioHTTPClient
from wonda.modules import logger
from wonda.types.methods import APIMethods


class API(ABCAPI, APIMethods):
    def __init__(
        self,
        token: Token,
        http_client: Optional[ABCHTTPClient] = None,
    ) -> None:
        super().__init__(self)

        self.token = token
        self.http_client = http_client or AioHTTPClient()
        self.request_validators: List[ABCRequestValidator] = DEFAULT_REQUEST_VALIDATORS
        self.response_validators: List[
            ABCResponseValidator
        ] = DEFAULT_RESPONSE_VALIDATORS

    async def request(self, method: str, params: dict) -> APIResponse:
        logger.debug(f"Calling {method} with {params}")

        data = await self.validate_request(params)
        response = await self.http_client.request_json(
            method="post", url=self.api_url + method, data=data
        )

        logger.debug(f"Server responded {response}")
        return await self.validate_response(method, params, response)

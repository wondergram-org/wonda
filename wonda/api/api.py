from typing import List, Optional

from wonda.api.abc import ABCAPI, APIResponse
from wonda.api.request_validator import (
    DEFAULT_REQUEST_VALIDATORS,
    ABCRequestValidator,
)
from wonda.api.response_validator import (
    DEFAULT_RESPONSE_VALIDATORS,
    ABCResponseValidator,
)
from wonda.api.utils import Token
from wonda.http.abc import ABCHTTPClient
from wonda.http.aiohttp import AioHTTPClient
from wonda.modules import logger
from wonda.types.methods import APIMethods


class API(ABCAPI, APIMethods):
    def __init__(
        self,
        token: Token,
        ignore_errors: bool = False,
        http_client: Optional[ABCHTTPClient] = None,
    ) -> None:
        super().__init__(self)

        self.token = token
        self.ignore_errors = ignore_errors
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

    async def validate_request(self, request: dict) -> dict:
        """
        Performs request validation. Can modify
        sent data in place.
        """
        for validator in self.request_validators:
            request = await validator.validate(request)
        return request

    async def validate_response(
        self, method: str, data: dict, response: dict
    ) -> APIResponse:
        """
        Verifies and adapts the response.
        """
        for validator in self.response_validators:
            response = await validator.validate(method, data, response, self)
        return response

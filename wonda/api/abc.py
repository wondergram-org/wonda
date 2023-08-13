import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:
    from wonda.api import ABCRequestValidator, ABCResponseValidator, Token
    from wonda.net import ABCNetworkClient

APIRequest = typing.NamedTuple("APIRequest", [("method", str), ("params", dict)])


class ABCAPI(ABC):
    API_URL = "https://api.telegram.org/"
    APIRequest = APIRequest

    response_validators: list["type[ABCResponseValidator]"]
    request_validators: list["type[ABCRequestValidator]"]
    network_client: "ABCNetworkClient"
    token: "Token"

    @property
    def api_url(self) -> str:
        """
        Address for API requests
        """
        return self.API_URL + f"bot{self.token}/"

    @property
    def file_url(self) -> str:
        """
        Link to the file storage
        """
        return self.API_URL + f"file/bot{self.token}/"

    @abstractmethod
    async def request(self, method: str, params: dict = {}) -> bytes:
        """
        Opens a request session and makes a single API call
        """

    async def request_many(
        self, requests: typing.Iterable[APIRequest]  # type: ignore
    ) -> typing.AsyncIterator[bytes | None]:
        """
        Makes multiple calls to the API opening session for each
        """
        for request in requests:
            yield await self.request(request.method, request.params)  # type: ignore

    async def validate_request(self, params: dict) -> dict | None:
        """
        Performs validation of the request data.
        If necessary, modifies and transforms it.
        """
        for v in self.request_validators:
            params = await v(self.network_client).validate(params)
        return params

    async def validate_response(self, response: bytes) -> bytes:
        """
        Verifies and adapts the response.
        """
        for v in self.response_validators:
            response = await v(self).validate(response)
        return response

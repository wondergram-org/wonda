import typing
from abc import ABC, abstractmethod

if typing.TYPE_CHECKING:
    from wonda.api import ABCRequestValidator, ABCResponseValidator, Token
    from wonda.http import ABCHTTPClient

APIResponse = typing.NewType(
    "APIResponse", typing.Union[typing.NoReturn, typing.Dict[str, typing.Any]]
)
APIRequest = typing.NamedTuple("APIRequest", [("method", str), ("params", dict)])


class ABCAPI(ABC):
    API_URL = "https://api.telegram.org/"
    APIRequest = APIRequest

    response_validators: typing.List["ABCResponseValidator"]
    request_validators: typing.List["ABCRequestValidator"]
    http_client: "ABCHTTPClient"
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
    async def request(
        self, method: str, params: typing.Optional[dict] = None
    ) -> APIResponse:
        """
        Opens a request session and makes a single API call
        """
        pass

    async def request_many(
        self, requests: typing.Iterable[APIRequest]
    ) -> typing.AsyncIterator[APIResponse]:
        """
        Makes multiple calls to the API opening session for each
        """
        for request in requests:
            yield await self.request(request.method, request.params)

    async def validate_request(self, request: dict) -> dict:
        """
        Performs validation of the request data.
        If necessary, modifies and transforms it.
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

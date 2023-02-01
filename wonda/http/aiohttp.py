import ssl
from asyncio import AbstractEventLoop, get_event_loop
from typing import TYPE_CHECKING, Optional

import certifi
from aiohttp import ClientSession, ClientTimeout, TCPConnector

from wonda.http.abc import ABCHTTPClient
from wonda.modules import JSONModule, json

if TYPE_CHECKING:
    from aiohttp import ClientResponse


class AioHTTPClient(ABCHTTPClient):
    def __init__(
        self,
        loop: Optional[AbstractEventLoop] = None,
        session: Optional[ClientSession] = None,
        timeout: Optional[ClientTimeout] = None,
        json_processing_module: Optional[JSONModule] = None,
        **kwargs,
    ):
        self.loop = loop or get_event_loop()

        self.session = session
        self.session_params = kwargs
        self.json_processing_module = json_processing_module or json
        self.timeout = timeout or ClientTimeout(0)
        self.ssl = ssl.create_default_context(cafile=certifi.where())

    async def request_raw(
        self, url: str, method: str = "GET", data: Optional[dict] = None, **kwargs
    ) -> "ClientResponse":
        if not self.session:
            connector = TCPConnector(ssl=self.ssl)
            self.session = ClientSession(
                connector=connector,
                json_serialize=self.json_processing_module.dumps,
                **self.session_params,
            )

        async with self.session.request(
            url=url, method=method, data=data, **kwargs
        ) as response:
            await response.read()
            return response

    async def request_json(
        self, url: str, method: str = "GET", data: Optional[dict] = None, **kwargs
    ) -> dict:
        response = await self.request_raw(url, method, data, **kwargs)
        return await response.json(
            encoding="utf-8", loads=self.json_processing_module.loads, content_type=None
        )

    async def request_text(
        self, url: str, method: str = "GET", data: Optional[dict] = None, **kwargs
    ) -> str:
        response = await self.request_raw(url, method, data, **kwargs)
        return await response.text(encoding="utf-8")

    async def request_content(
        self, url: str, method: str = "GET", data: Optional[dict] = None, **kwargs
    ) -> bytes:
        response = await self.request_raw(url, method, data, **kwargs)
        return response._body

    async def close(self) -> None:
        if self.session and not self.session.closed:
            await self.session.close()

    def __del__(self):
        if self.session and not self.session.closed:
            if self.session._connector is not None and self.session._connector_owner:
                self.session._connector.close()
            self.session._connector = None

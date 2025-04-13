import ssl

import certifi
from aiohttp import ClientSession, ClientTimeout, FormData, TCPConnector

from wonda.net.abc import ABCNetworkClient
from wonda.net.utils import json


class DefaultNetworkClient(ABCNetworkClient):
    def __init__(
        self, session: ClientSession | None = None, timeout: ClientTimeout | None = None
    ) -> None:
        self.timeout = timeout or ClientTimeout(0)
        self.session = session

    async def request_bytes(
        self, url: str, method: str = "get", data: dict | None = None, **kwargs
    ) -> bytes:
        if not self.session:
            connector = TCPConnector(
                ssl=ssl.create_default_context(cafile=certifi.where())
            )
            self.session = ClientSession(
                json_serialize=json.dumps, timeout=self.timeout, connector=connector
            )

        async with self.session.request(
            url=url, method=method, data=data, **kwargs
        ) as response:
            return await response.content.read()

    async def request_json(
        self, url: str, method: str = "get", data: dict | None = None, **kwargs
    ) -> dict:
        response = await self.request_bytes(url, method, data, **kwargs)
        return json.loads(response)

    async def request_text(
        self, url: str, method: str = "get", data: dict | None = None, **kwargs
    ) -> str:
        response = await self.request_bytes(url, method, data, **kwargs)
        return response.decode()

    async def close(self) -> None:
        if self.session and not self.session.closed:
            await self.session.close()

    @staticmethod
    def construct_form(data: dict) -> FormData:
        form = FormData()
        for k, v in data.items():
            params = {}
            if isinstance(v, int):
                v = str(v)
            elif isinstance(v, tuple):
                params["filename"], v = v[0], v[1]
            form.add_field(k, v, **params)
        return form

    def __del__(self):
        if self.session and not self.session.closed:
            if self.session._connector is not None and self.session._connector_owner:
                self.session._connector.close()
            self.session._connector = None

import ssl

import certifi
from aiohttp import ClientSession, ClientTimeout, FormData, TCPConnector

from wonda.modules import JSONModule, json
from wonda.net.abc import ABCNetworkClient


class DefaultNetworkClient(ABCNetworkClient):
    def __init__(
        self,
        session: ClientSession | None = None,
        json_processing_module: JSONModule | None = None,
        timeout: ClientTimeout | None = None,
    ) -> None:
        self.json_processing_module = json_processing_module or json
        self.session = session or ClientSession(
            timeout=timeout or ClientTimeout(0),
            connector=TCPConnector(
                ssl=ssl.create_default_context(cafile=certifi.where())
            ),
            json_serialize=self.json_processing_module.dumps,
        )

    async def request_bytes(
        self, url: str, method: str = "get", data: dict | None = None, **kw
    ) -> bytes:
        async with self.session.request(
            url=url, method=method, data=data, **kw
        ) as response:
            return await response.content.read()

    async def request_json(
        self, url: str, method: str = "get", data: dict | None = None, **kw
    ) -> dict:
        response = await self.request_bytes(url, method, data, **kw)
        return self.json_processing_module.loads(response)

    async def request_text(
        self, url: str, method: str = "get", data: dict | None = None, **kw
    ) -> str:
        response = await self.request_bytes(url, method, data, **kw)
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

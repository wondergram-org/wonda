from asyncio import run

from wonda import API, DefaultPolling, Token
from wonda.modules import logger

polling = DefaultPolling(API(Token.from_env()))


async def main():
    async for update in polling.listen():
        await logger.debug("Handling", update=update)


run(main())

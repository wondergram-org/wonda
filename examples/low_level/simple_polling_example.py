from asyncio import run

from wonda import API, DefaultPoller, Token
from wonda.modules import logger

polling = DefaultPoller(API(Token.from_env()))


async def main():
    async for update in polling.listen():
        await logger.debug("Handling", update=update)


run(main())

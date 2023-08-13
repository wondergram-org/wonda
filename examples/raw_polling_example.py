from asyncio import run

from wonda import API, Poller, Token
from wonda.modules import logger

api = API(Token.from_env())


async def main():
    poller = Poller(api)

    async for update in poller.poll():
        await logger.debug("Handling", update=update)


run(main())

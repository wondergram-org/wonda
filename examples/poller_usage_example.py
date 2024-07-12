from wonda import API, DefaultPoller, Token
from wonda.modules import logger

# Make an API with a token from an environment variable.
api = API(Token.from_env())


async def main():
    # Pass an API object to grab updates from.
    poller = DefaultPoller(api)

    # You can specify exactly which types of updates
    # you wish to receive via this poller.
    poller.options.allowed_updates = ["message", "callback_query", "inline_query"]

    # Iterate through new updates as they come.
    async for update in poller.poll():
        await logger.ainfo("Handling", update=update)


# Run an example function in the current event loop.
__import__("asyncio").get_event_loop().run_until_complete(main())

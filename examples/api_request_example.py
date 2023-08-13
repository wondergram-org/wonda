from wonda.api import API, Token

# Make an API with a token from an environment variable.
api = API(Token.from_env())


async def main() -> None:
    # Make a single API request.
    print(await api.request("getMe", {}))

    # Make multiple API requests opening session for each.
    async for response in api.request_many(
        [api.APIRequest("getMe", {}), api.APIRequest("getUpdates", {})]
    ):
        print(response)


# Run an example function in the current event loop.
__import__("asyncio").get_event_loop().run_until_complete(main())

from wonda import API, APIException, Token

# Make an API with a token from an environment variable.
api = API(Token.from_env())


async def main() -> None:
    try:
        await api.send_message("Hi bestie!", 1)
    except APIException[400]:
        print("Oops, bad request.")
    except APIException[401, 404]:
        print("Oops, unauthorized.")
    except APIException as e:
        print(f"An error {e.code} occured.")


# Run an example function in the current event loop.
__import__("asyncio").get_event_loop().run_until_complete(main())

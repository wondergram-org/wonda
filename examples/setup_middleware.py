from wonda import ABCMiddleware, Bot, Message, Token
from wonda.bot.rules import Command
from wonda.types.objects import User

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


class SimpleMiddleware(ABCMiddleware[Message]):
    async def pre(self, m: Message, ctx: dict) -> bool:
        # The purpose of this method is to filter updates based on
        # the defined condition. An update for which it returns
        # `False` will not be processed.

        # You can send values to the context so they can be
        # later available for use in handler functions.
        ctx["user"] = m.from_

        # Return `True` so this update can be processed.
        return True

    async def post(self, m: Message, ctx: dict, responses: list) -> None:
        # This method will be called after the update is handled.
        # Use it to perform clean up, log various info
        # and work with handler responses.
        await m.answer(f"Update handled with {ctx=} {responses=}")


@bot.on.message(Command("profile"))
async def profile_handler(m: Message, user: User) -> None:
    """
    A simple handler to prove that middleware
    are working nice and sound.
    """
    await m.answer("I remember you! You are " + user.first_name.capitalize() + "!")


# Register our custom middleware in the view.
bot.on.message.register_middleware(SimpleMiddleware())

# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

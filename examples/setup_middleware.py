from wonda import ABCMiddleware, Bot, Message, Token
from wonda.bot.rules import Command
from wonda.types.objects import User

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


class SimpleMiddleware(ABCMiddleware[Message]):
    async def pre(self, m: Message, ctx: dict) -> bool:
        # The purpose of this method is to filter updates based on
        # the rules you define. An update for which this function
        # returns `False` will not be processed.

        # You can also send values to context so they can be
        # later available in handler functions for you to
        # interact with.
        ctx["user"] = m.from_

        # Return `True` so this update can be processed.
        return True

    async def post(self, m: Message, ctx: dict, responses: list) -> None:
        # This method will be called after the update is handled.
        # Use it to clean up interactions, log various info
        # and manipulate handler responses.
        await m.answer(f"Update handled with {ctx=} {responses=}")


@bot.on.message(Command("profile"))
async def profile_handler(m: Message, user: User) -> None:
    """
    A simple handler to proof that middleware
    are working nice and sound.
    """
    first_name = user.first_name.capitalize()
    await m.answer(f"I remember you! {first_name} you are!")


# Add our freshly made middleware to the view.
bot.dispatcher.message.middlewares.append(SimpleMiddleware())

# Run the bot. This function uses `.run_polling()` under the hood to start receiving updates.
# It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

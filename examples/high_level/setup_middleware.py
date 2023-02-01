from wonda import BaseMiddleware, Bot, Message, Token
from wonda.bot.rules import Command
from wonda.types.objects import User

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


@bot.labeler.message_view.register_middleware
class SimpleMiddleware(BaseMiddleware[Message]):
    async def pre(self) -> None:
        # This middleware will be called before all handlers.
        # It can be used for registering users, validating update data, etc.
        await self.update.answer("Hello, world!")

    async def post(self) -> None:
        # This middleware will be called after all handlers. It can be used
        # for logging and analyzing after update is processed.
        await self.update.answer("Goodbye, world!")


@bot.labeler.message_view.register_middleware
class PassthroughMiddleware(BaseMiddleware[Message]):
    # You can actually have any number of pre and post middlewares.

    async def pre(self) -> None:
        # You might need to pass an argument from middleware to the handlers,
        # for example, while registering a user. To do that, use `self.send()` method.
        # If you need to stop processing the update altogether, use `self.stop()`.
        if self.update.from_.is_bot:
            self.stop("Messages from bots are not allowed to be handled.")

        self.send({"user": self.update.from_})

    async def post(self) -> None:
        # As was discussed before, post middlewares are used
        # primarily for collecting and logging data. So let's print
        # a view and a list of handlers message was processed with.
        await self.update.answer(
            "Message was processed with {0} view and {1} handlers.".format(
                self.view, ", ".join(str(i) for i in self.handlers)
            )
        )


@bot.on.message(Command("profile"))
async def who_am_i_handler(_, user: User) -> str:
    """
    A simple handler to proof that middleware
    are working nice and sound.
    """
    first_name = user.first_name.capitalize()
    return f"I remember you! {first_name} you are!"


# Run loop > loop.run_forever() > with tasks created in loop_wrapper before.
# The main polling task for bot is bot.run_polling()
bot.run_forever()

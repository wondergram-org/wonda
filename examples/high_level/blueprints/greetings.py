from wonda import Blueprint, Message
from wonda.bot.rules import Text

# Make a blueprint of a bot.
bp = Blueprint()


@bp.on.message(Text(["hi", "hello", "hey"], ignore_case=True))
async def hi_handler(m: Message) -> None:
    await m.answer("Glad to see you!")


@bp.on.message(
    Text(["good morning", "good afternoon", "good evening"], ignore_case=True)
)
async def hello_handler(m: Message) -> None:
    await m.answer("Welcome!")

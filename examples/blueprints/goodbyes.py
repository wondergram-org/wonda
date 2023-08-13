from wonda import Blueprint, Message
from wonda.bot.rules import Text

# Make a blueprint of a bot.
bp = Blueprint()


@bp.on.message(Text(["bye", "cheers"], ignore_case=True))
async def bye_handler(m: Message) -> None:
    await m.answer("See you soon!")


@bp.on.message(Text(["take care", "have a good day"], ignore_case=True))
async def goodbye_handler(m: Message) -> None:
    await m.answer("You too, bye!")

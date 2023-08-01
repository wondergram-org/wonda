from wonda import Blueprint
from wonda.bot.rules import Text

# Make a blueprint of a bot.
bp = Blueprint()


@bp.on.message(Text(["bye", "cheers"], ignore_case=True))
async def bye_handler(_) -> str:
    return "See you soon!"


@bp.on.message(Text(["take care", "have a good day"], ignore_case=True))
async def goodbye_handler(_) -> str:
    return "You too, bye!"

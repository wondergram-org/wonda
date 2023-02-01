from wonda import BotBlueprint
from wonda.bot.rules import Text

# Make a blueprint of a bot.
bp = BotBlueprint()


@bp.on.message(Text(["hi", "hello", "hey"], ignore_case=True))
async def hi_handler(_) -> str:
    return "Glad to see you!"


@bp.on.message(
    Text(["good morning", "good afternoon", "good evening"], ignore_case=True)
)
async def hello_handler(_) -> str:
    return "Welcome!"

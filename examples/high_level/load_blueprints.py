from wonda import Bot, Token

# Make a bot with a token from an environment variable.
# You should provide API to bot before constructing blueprints,
# otherwise they won't have it.
bot = Bot(Token.from_env())

# Load blueprints directly from `blueprints` package.
from .blueprints import bps

# Iterate over a list of blueprints and register them.
for bp in bps:
    # Register a blueprint via <.load_into()> method. This will load the blueprint's dispatcher
    # into the dispatcher of the given framework and then return blueprint constructed with
    # framework's API and dispatcher.
    bp.load_into(bot)


# Run the bot. This function uses `.run_polling()` under the hood to start receiving updates.
# It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

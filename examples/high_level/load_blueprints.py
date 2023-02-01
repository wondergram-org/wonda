from wonda import Bot, Token

# Make a bot with a token from an environment variable.
# You should provide API to bot before constructing blueprints,
# otherwise they won't have it.
bot = Bot(Token.from_env())

# Load blueprints directly from `blueprints` package.
from .blueprints import bps

# Iterate over a list of blueprints and register them.
for bp in bps:
    # Register a blueprint via <.load()> method. This will load the blueprint's labeler
    # into the labeler of the given framework and then return blueprint constructed with
    # framework's API and polling.
    bp.load(bot)

# Run loop > loop.run_forever() > with tasks created in loop_wrapper before.
# The main polling task for bot is bot.run_polling()
bot.run_forever()

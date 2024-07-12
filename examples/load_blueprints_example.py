from wonda import Bot, Token

# Load blueprints directly from `blueprints` package.
from blueprints import bps


# Make a bot with a token from an environment variable.
# You should provide it to the bot before constructing
# blueprints, otherwise they won't be able to use 
# the API.
bot = Bot(Token.from_env())

# Iterate over a list of blueprints and register them.
for bp in bps:
    # Register a blueprint via `.load_into()` method. This loads
    # every handler registered in `bp` in the `bot` and then
    # sets API and state manager for `bp`.
    bp.load_into(bot)

# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

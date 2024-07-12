from wonda import Bot, File, Message, Token
from wonda.bot.rules import Command
from wonda.contrib.middleware import RateLimitingMiddleware
from wonda.tools.storage import MemoryExpiringStorage

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


@bot.on.message(Command("special"))
async def special_cmd_handler(m: Message) -> None:
    # This sticker gets sent only if the user respects our rate limit.
    await m.ctx_api.send_sticker(
        chat_id=m.chat.id, sticker=File.from_path("examples/assets/cat.jpeg")
    )


# Register a rate limiting middleware with an expiration of 5 seconds
# and in-memory expiring storage.
bot.on.message.register_middleware(RateLimitingMiddleware(5, MemoryExpiringStorage()))

# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

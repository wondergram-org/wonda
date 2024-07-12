from wonda import Bot, BusinessConnection, Message, Token
from wonda.bot.rules import Command

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


@bot.on.business_connection()
async def business_connection_handler(business_connection: BusinessConnection) -> None:
    status = "connected to" if business_connection.is_enabled else "disconnected from"

    await business_connection.ctx_api.send_message(
        f"This bot just got {status} your user", business_connection.user_chat_id
    )


@bot.on.business_message(Command("business"))
async def business_handler(m: Message) -> None:
    await m.answer(
        "This message was handled by a bot built on Wonda via a business connection!"
    )


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

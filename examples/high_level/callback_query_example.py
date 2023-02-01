from wonda import Bot, Token
from wonda.bot.rules import Command, Data
from wonda.bot.updates import BotUpdateType, CallbackQuery, Message
from wonda.tools.keyboard import Callback, InlineKeyboard

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())

# Create an inline keyboard with a button that will be used to trigger a callback.
INLINE_KEYBOARD = (
    InlineKeyboard()
    .add(Callback("🍎 Apple", "apple"))
    .add(Callback("🍊 Orange", "orange"))
    .row()
    .add(Callback("I don't want to choose", "stop"))
    .build()
)


@bot.on.message(Command("start"))
async def start_handler(msg: Message) -> None:
    # This is a handler that sends a simple inline keyboard
    # containing three buttons with their respective callback data.
    await msg.answer(
        "Pick any of these fruits on the keyboard!",
        reply_markup=INLINE_KEYBOARD,
    )


@bot.on.raw_update(
    BotUpdateType.CALLBACK_QUERY, CallbackQuery, Data(["apple", "orange"])
)
async def fruit_handler(upd: CallbackQuery) -> None:
    # Answer a callback query <.answer()> method. To display
    # an alert, pass `show_alert` param.
    await upd.answer(
        "You chose a fruit! Fruits are healthy and delicious 🍋", show_alert=True
    )


@bot.on.raw_update(BotUpdateType.CALLBACK_QUERY, CallbackQuery, Data("stop"))
async def shoe_handler(upd: CallbackQuery) -> None:
    await upd.ctx_api.edit_message_text(
        "That's ok. Some choices are just too hard to make.",
        message_id=upd.message.message_id,
        chat_id=upd.message.chat.id,
    )


# Run loop > loop.run_forever() > with tasks created in loop_wrapper before.
# The main polling task for bot is bot.run_polling()
bot.run_forever()

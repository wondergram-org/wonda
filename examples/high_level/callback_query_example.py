from wonda import Bot, Token
from wonda.bot.rules import CallbackData, Command
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
    .add(Callback("👟 Shoe", "shoe"))
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
    BotUpdateType.CALLBACK_QUERY, CallbackQuery, CallbackData(["apple", "orange"])
)
async def fruit_handler(upd: CallbackQuery) -> None:
    # To answer to a callback query, you can use <.answer()> method.
    # This would result in a small message showing up the screen.
    await upd.answer("You chose a fruit! Fruits are healthy and delicious 🍋")


@bot.on.raw_update(BotUpdateType.CALLBACK_QUERY, CallbackQuery, CallbackData("shoe"))
async def shoe_handler(upd: CallbackQuery) -> None:
    # If you need to grab user's attention, you can display an alert
    # with the content you want to show. To do that, pass `show_alert`
    # parameter to the <.answer()> method.
    await upd.answer("You chose a shoe! What the fuck", show_alert=True)


# Run loop > loop.run_forever() > with tasks created in loop_wrapper before.
# The main polling task for bot is bot.run_polling()
bot.run_forever()

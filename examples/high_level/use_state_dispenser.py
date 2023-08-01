from wonda import BaseStateGroup, Bot, Message, Token
from wonda.bot.rules import Command, State, Text
from wonda.tools.keyboard import Button, ReplyKeyboardBuilder

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


# Create a new state group describing the flow of the conversation.
class MenuState(BaseStateGroup):
    START = "start"
    BUY = "buy"


MENU_KEYBOARD = (
    ReplyKeyboardBuilder(resize_keyboard=True)
    .add(Button("About us"))
    .add(Button("Buy a drink"))
    .build()
)
BEVERAGE_KEYBOARD = (
    ReplyKeyboardBuilder(one_time_keyboard=True, resize_keyboard=True)
    .add(Button("Espresso"))
    .add(Button("Cappuccino"))
    .build()
)


@bot.on.message(Command(["start", "return"]))
async def menu_handler(msg: Message) -> None:
    await msg.answer(
        "Welcome to our coffee house! What can we make for you today?",
        reply_markup=MENU_KEYBOARD,
    )
    await bot.state_dispenser.set(msg.chat.id, MenuState.START)


@bot.on.message(Text("about us", ignore_case=True) & State(MenuState.START))
async def about_us_handler(msg: Message) -> None:
    await msg.answer(
        "We only opened a couple years ago, but are already selling "
        "tasty coffee of exceptional quality. People love it here, "
        "and we think you will too."
    )


@bot.on.message(Text("buy a drink", ignore_case=True) & State(MenuState.START))
async def buy_drink_handler(msg: Message) -> None:
    await msg.answer(
        "We sure have 'em in stock! Choose a beverage "
        "or just /return to menu if you don't want anything.",
        reply_markup=BEVERAGE_KEYBOARD,
    )
    await bot.state_dispenser.set(msg.chat.id, MenuState.BUY)


@bot.on.message(
    Text(["cappuccino", "espresso"], ignore_case=True) & State(MenuState.BUY)
)
async def choose_beverage_handler(msg: Message) -> None:
    await msg.answer(
        f"Thanks! An order for {msg.text} is now placed. "
        "It'll be ready in a couple of minutes. You can /return to menu."
    )


# Run the bot. This function uses `.run_polling()` under the hood to start receiving updates.
# It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

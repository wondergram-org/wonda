from wonda import BaseStateGroup, Bot, Message, Token, rules
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

@bot.on.message(rules.Command("start", "return"))
async def menu_handler(m: Message) -> None:
    await m.answer(
        "Welcome to our coffee house! What can we make for you today?",
        reply_markup=MENU_KEYBOARD,
    )
    await bot.state_manager.set(m.chat.id, MenuState.START)


@bot.on.message(rules.State(MenuState.START) & rules.Text("about us", ignore_case=True))
async def about_us_handler(m: Message) -> None:
    await m.answer(
        "We only opened a couple years ago, but are already selling "
        "tasty coffee of exceptional quality. People love it here, "
        "and we think you will too."
    )


@bot.on.message(
    rules.State(MenuState.START) & rules.Text("buy a drink", ignore_case=True)
)
async def buy_drink_handler(m: Message) -> None:
    await m.answer(
        "We sure have 'em in stock! Choose a beverage "
        "or just /return to menu if you don't want anything.",
        reply_markup=BEVERAGE_KEYBOARD,
    )
    await bot.state_manager.set(m.chat.id, MenuState.BUY)


@bot.on.message(
    rules.State(MenuState.BUY) & rules.Text("cappuccino", "espresso", ignore_case=True)
)
async def choose_beverage_handler(m: Message) -> None:
    await m.answer(
        f"Thanks! An order for {m.text} is now placed. "
        "It'll be ready in a couple of minutes. You can /return to menu."
    )


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

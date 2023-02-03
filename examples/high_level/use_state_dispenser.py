from wonda import BaseStateGroup, Bot, Message, Token
from wonda.bot.rules import Command, State, Text
from wonda.tools.keyboard import Button, ReplyKeyboard

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())

# Create a new state group describing the flow of the conversation.
class MenuState(BaseStateGroup):
    START = "start"
    BUY = "buy"


MENU_KEYBOARD = (
    ReplyKeyboard().add(Button("About us")).add(Button("Buy a drink")).build()
)
BEVERAGE_KEYBOARD = (
    ReplyKeyboard().add(Button("Espresso")).add(Button("Cappuccino")).add().build()
)


@bot.on.message(Command("start") | Command("return"))
async def menu_handler(msg: Message) -> None:
    await msg.answer(
        "Welcome to our coffee house! What can we make for you today?",
        reply_markup=MENU_KEYBOARD,
    )
    await bot.state_dispenser.set(msg.chat.id, MenuState.START)


@bot.on.message(Text("about us", ignore_case=True) & State(MenuState.START))
async def about_us_handler(msg: Message) -> None:
    await msg.answer(
        "Our company was founded all the way back into seventies. "
        "We were inspired to sell high-quality coffee and other goods. "
        "Now we serve espresso, latte, juices and drinks, both hot and cold.\n\n"
    )


@bot.on.message(
    Text("buy a drink", ignore_case=True) & State(MenuState.START),
)
async def buy_drink_handler(msg: Message) -> None:
    await msg.answer(
        "We sure have 'em in stock! Choose a beverage "
        "or just /return to menu if you don't want anything.",
        reply_markup=BEVERAGE_KEYBOARD,
    )
    await bot.state_dispenser.set(msg.chat.id, MenuState.BUY)


@bot.on.message(
    Text(["cappuccino", "espresso"], ignore_case=True), State(MenuState.BUY)
)
async def choose_beverage_handler(msg: Message) -> None:
    await msg.answer(
        f"Thanks! The order for {msg.text} is now placed. "
        "It'll be ready in a couple of minutes. You can /return to menu."
    )


# Run loop > loop.run_forever() > with tasks created in loop_wrapper before.
# The main polling task for bot is bot.run_polling()
bot.run_forever()

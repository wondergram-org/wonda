from wonda import Bot, Message, Token
from wonda.bot.rules import ABCRule, Command, From, IsPrivate, Text

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())

# You can add any rule as an auto rule.
# It means that it will be automatically applied
# to all handlers in the context of current dispatcher.
# E.g. bot.dispatcher.message.auto_rules.append(SomeRule())


# Define a custom rule which implements asynchronous check method.
class HasPhoto(ABCRule[Message]):
    async def check(self, msg: Message, _) -> bool:
        # Check if the message has a photo.
        return bool(msg.photo)


@bot.on.message(
    # If any of these rules are satisfied,
    Command("start") | Text(["hi", "hello"]),
    # both of these are satisfied too
    IsPrivate() & From("wndrgrm"),
    # and this rule is not
    ~HasPhoto(),
)
async def advanced_handler(msg: Message) -> None:
    # ..then the message will be handled successfully.
    await msg.answer("You've made it here! Congratulations!")


# Run the bot. This function uses `.run_polling()` under the hood to start receiving updates.
# It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

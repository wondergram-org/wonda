# Rules are a crucial part of the framework - they help handle updates
# and filter out the updates that do not conform to some condition.
# This example features their advanced use cases.
#
# It may not be what you're looking for. If you're looking for
# simple use cases for rules, please, read `basic_bot_example.py`.

from wonda import Bot, Message, Token
from wonda.bot.rules import ABCRule, Command, From, Function, Has, IsPrivate, Text

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())

# A rule can be configured to be checked each time
# an update comes through. It will apply to all handlers
# that you declare in the context of a dispatcher. Example:
# bot.on.message.auto_rules.append(IsReply())


# Define a custom rule which implements asynchronous check method.
class HasPhoto(ABCRule[Message]):
    async def check(self, m: Message, _) -> bool:
        return bool(m.photo)


@bot.on.message(
    # If any of these rules are satisfied,
    Command("start") | Text("hi", "hello"),
    # both of these are satisfied too
    IsPrivate() & HasPhoto(),
    # and this rule is not
    ~From("durov"),
)
async def advanced_handler(m: Message) -> None:
    # then this handler will be invoked. Try it out!
    await m.answer("Congratulations! You satisfied all the rules.")


# You can use the Has rule to check if the update object has some attributes.
@bot.on.message(Has("photo") | Has("video") | Has("audio"))
async def media_handler(m: Message) -> None:
    await m.reply("I sense some kind of media there..")


# Alternatively, you can define rules inline without having to implement a dedicated
# class. Use `Function` rule to build complex conditional statements to handle your
# updates. It accepts predicate functions that take in the update object and
# the handler context.
@bot.on.message(
    Function[Message](lambda m, _: m.text[-1] in ["a", "o", "i", "e", "u", "y"])
)
async def vowel_handler(m: Message) -> None:
    await m.answer("You typed something that ends in a vowel.")


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

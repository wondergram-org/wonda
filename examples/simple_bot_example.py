from wonda import Bot, TelegramAPIError, Token
from wonda.bot.rules import FromGroup, Fuzzy, Text, WasEdited
from wonda.bot.updates import ChatJoinRequest, Message

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


# A handler can be registered using the dispatcher. To handle various updates,
# use relevant decorators. To define special logic, use built-in rules
# or make your own, inheriting from wonda.bot.rules.abc.ABCRule.
@bot.on.message(Text(["hi", "hello", "howdy"]))
async def message_handler(m: Message) -> None:
    # Text rule matches the message text with the given list of strings.
    # If the match is successful, following lines will be executed.

    # This line will call shortcut method to answer a message from user
    # (see https://github.com/wondergram-org/wonda/blob/main/wonda/bot/updates/types.py#L43).
    await m.answer("Hello, friend!")


# A good example of how you can use this mechanic is to kick people that say
# bad words from the chat. Here we check if the message was not sent in private
# and that it contained some nasty things.
@bot.on.message(FromGroup(), Fuzzy(["shit", "fuck", "bastard", "asshole"]))
async def group_message_handler(m: Message) -> None:
    # Fuzzy rule measures the similarity ratio between two string sequences.
    # If the ratio is greater than or equal to set `min_ratio`,
    # following lines will be executed.

    try:
        # This is a basic API call. Please use ctx_api as it is always available
        # (that can't be said for bot API, for example, while using blueprints).
        await m.ctx_api.ban_chat_member(chat_id=m.chat.id, user_id=m.from_.id)
    except TelegramAPIError[400]:
        # Gracefully handle the error and make an apology.
        await m.answer("Sorry, can't kick this member because of an error.")


# Update types like `edited_message` are handled using the same decorator,
# as they all share the same model. To see if it was edited,
# for example, we can use yet another rule.
@bot.on.message(WasEdited())
async def edited_message_handler(m: Message) -> None:
    # This is a shortcut method to reply to a message from the user.
    # See line 20 to learn more.
    await m.reply("Hm? I heard you edited a message.")


# As was said previously, you can handle many updates besides messages.
# Most updates even have shortcut methods that ease interfacing with methods
# frequently used for those update types. To show this in action, let's answer
# a join request to a dog chat in which only good boys are allowed.
@bot.on.chat_join_request()
async def chat_join_request_handler(req: ChatJoinRequest) -> None:
    # Verify that the user who sent the request is actually a dog
    # and approve the request.
    if any(word in ("woof", "bark", "ruff") for word in (req.bio or "").split()):
        await req.approve()
        return
    # If the user turned out to be a human, reject the request.
    await req.decline()


# Run the bot. This function uses `.run_polling()` under the hood to start receiving updates.
# It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

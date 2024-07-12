from wonda import APIException, Bot, Token
from wonda.bot.rules import FromGroup, Function, Fuzzy, Text, WasEdited
from wonda.bot.updates import ChatJoinRequest, Message

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


# A handler can be registered via the dispatcher. To handle various updates
# use relevant decorators. Special logic can be implemented using
# built-in rules or by making your own rules with
# `wonda.bot.rules.abc.ABCRule`.
@bot.on.message(Text("hi", "hello", "howdy"))
async def message_handler(m: Message) -> None:
    # Text rule matches message text with the given list of strings.
    # If the match is successful, following lines will be executed.

    # This line will call a shortcut method to answer a message from user
    # (see https://github.com/wondergram-org/wonda/blob/main/wonda/bot/updates/types.py#L54).
    await m.answer("Hello, friend!")


# A good example of how you can use this mechanic is to kick people that say
# undesirable things from the chat. Here we check if the message was sent
# in a group and that it contained some bad words.
@bot.on.message(FromGroup() & Fuzzy("shit", "bitch", "fuck", "bastard"))
async def group_message_handler(m: Message) -> None:
    # `Fuzzy` rule measures how similar the text is to the texts you've listed.
    # If the similarity ratio meets a pre-determined threshold, this handler is invoked.

    try:
        # This is a basic request to the API. The API is available from
        # the bot interface, the blueprint interface and update models.
        await m.ctx_api.ban_chat_member(chat_id=m.chat.id, user_id=m.from_.id)
    except APIException[400]:
        # Here we handle an exception which has code 400.
        await m.answer("Sorry, I can't kick this member because of an error.")


# Wonda has no dedicated handlers for updates like `edited_message`
# and `edited_channel_post`. Instead, it uses rules to distinguish
# subtle changes to the update. Here we handle an edited message
# post using the `WasEdited` rule.
# This rule is universal across all message views, so it works not only for
# regular messages, but also channel posts and business messages.
@bot.on.channel_post(WasEdited())
async def edited_post_handler(m: Message) -> None:
    await m.reply("Did you catch that? This post was just edited!")


# You can also handle messages sent via business connections.
# Curious how the `Function` rule works? Check out `advanced_usage_example.py`.
@bot.on.business_message(Function[Message](lambda m, _: "order" in m.text))
async def business_message_handler(m: Message) -> None:
    await m.answer(
        "Hi! This is an automated reply. Your order will be ready "
        "in 3 to 5 business days. Thanks for choosing us!"
    )


# You can handle many updates besides messages. These updates have shortcut methods
# that ease interfacing with the API. To show this in action, let's answer
# a join request via a simple shortcut.
@bot.on.chat_join_request()
async def puppy_check_handler(req: ChatJoinRequest) -> None:
    # Verify that the user who sent the request is actually a dog
    # and approve the request.
    if any(word in ("woof", "bark", "ruff") for word in (req.bio or "").split()):
        await req.approve()
        return
    # If the user turned out to be a human, reject the request.
    await req.decline()


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

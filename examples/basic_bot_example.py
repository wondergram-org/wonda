from wonda import APIException, Bot, ChatJoinRequest, Message, Token, rules

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


# A handler for an update can be registered via the dispatcher. To handle various
# updates, use relevant decorators. You can implement special logic for
# the handler using rules, and you can make your own rules with
# `wonda.bot.rules.abc.ABCRule`.
@bot.on.message(
    # Matches text of the update with a given list of strings. If the text matches
    # any of those strings, the handler is executed.
    rules.Text("hi", "hello", "howdy")
)
async def message_handler(m: Message) -> None:
    # This line employs a shortcut to send an answer to the user. There are many
    # shortcuts suited for various actions, like replying to or forwarding a message
    # (https://github.com/wondergram-org/wonda/blob/main/wonda/bot/updates/types.py#L65)
    await m.answer("Hello, friend!")


# You can combine rules into chains to create complex logic for handling updates.
# Here's an example of using this mechanic to kick people that say
# undesirable things from the chat.
@bot.on.message(
    # Checks if the update was sent in a group. You can also check if the message
    # was sent in private using `IsPrivate` or in a channel using `FromChannel`.
    rules.FromGroup()
    # Measures similarity between the update text and a list of strings.
    # If the similarity ratio is in a specified threshold, this handler is executed.
    & rules.Fuzzy("shit", "bitch", "fuck", "bastard")
)
async def group_message_handler(m: Message) -> None:
    try:
        # A basic request to the API. The API is available from
        # the bot interface, the blueprint interface and update models.
        await m.ctx_api.ban_chat_member(chat_id=m.chat.id, user_id=m.from_.id)
    except APIException[400]:
        # Handle an exception with code 400.
        await m.answer("Sorry, I can't kick this member because of an error.")


# Updates of the same type are homogenized in a single decorator, meaning
# there are no dedicated decorators for updates like `edited_message`
# or `edited_channel_post`.
# Thanks to this homogenized architecture, message rules are versatile,
# meaning they can be used for regular messages as well as channel posts
# and business messages.
@bot.on.channel_post(
    # Determines whether a message has been modified.
    rules.WasEdited()
)
async def edited_post_handler(m: Message) -> None:
    await m.reply("Did you catch that? This post was just edited!")


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

from wonda import ActionSender, Bot, File, Message, Token, rules

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())

# Open a sample photo to be uploaded while sending a chat action.
picture = File.from_path("examples/assets/cat.jpeg")


@bot.on.message(rules.Command("start"))
async def start_handler(m: Message) -> None:
    # Initialize chat actions utility with the context API
    # bound to the update which we're handling.
    actions = ActionSender(m.ctx_api)

    # Simulate some sort of workload to keep our chat action sender busy.
    async with actions.upload_photo(m.chat.id):
        # Send the sample photo. This might take some time to complete
        # and while the user waits, the bot will send the `upload_photo`
        # chat action.
        await m.ctx_api.send_photo(picture, m.chat.id)


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

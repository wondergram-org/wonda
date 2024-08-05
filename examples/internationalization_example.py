from wonda import Bot, File, Message, Token, rules
from wonda.contrib.middleware import InternationalizationMiddleware
from wonda.tools.localization import DefaultLocalizator, Locale

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


@bot.on.message(rules.Command("greeting"))
async def greet_handler(m: Message, locale: Locale[str]) -> None:
    # Show the greeting message in the language the user has set in the app.
    await m.answer(
        "Responding in " + locale.name + ": " + locale.get_translation("greeting")
    )


@bot.on.message(rules.Command("cat"))
async def cat_handler(m: Message, locale: Locale[bytes]) -> None:
    # Get a cat photo according to the user language and turn it into a file
    # that can be uploaded to Telegram.
    photo = File.from_bytes(name="cat.jpg", source=locale.get_translation("cat"))

    await m.ctx_api.send_photo(
        photo=photo, chat_id=m.chat.id, caption="This cat speaks your language."
    )


@bot.on.message(rules.Command("farewell"))
async def bye_handler(m: Message, locale: Locale[str]) -> None:
    # Tip: set the `context_name` in the internationalization middleware below to `_`
    # to make this code even more compact.
    await m.answer(
        # We can use the locale object without ever touching `.get_translation()`,
        # because there is an alias which gets us the translation directly.
        locale("farewell")
    )


# Register the internationalization middleware so it can fetch a locale automatically.
bot.on.message.register_middleware(
    InternationalizationMiddleware(DefaultLocalizator("examples/assets/locales/"))
)


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

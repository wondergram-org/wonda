from wonda import Bot, Message, Token
from wonda.bot.rules import Command
from wonda.tools.text import Blockquote, Bold, Code, Italic, Link, Plain, Underline

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


@bot.on.message(Command("styling"))
async def styling_handler(m: Message) -> None:
    # You can decorate your text with whatever text styles are available in the API.
    # New styling options are quick and easy to implement. To implement a text style,
    # inherit from `wonda.tools.text.styling.styles.TextStyle`.
    decorations = (
        Plain("Text. Plain and simple. ")
        + Bold("This is a bold statement. ")
        + Italic("Mama mia! ")
        + Underline("Notice me!")
    )
    # This also includes blocks of text or code blocks. You can even nest other text styles
    # inside while being able to customize them!
    blocks = Blockquote(
        Link("Ernest Hemingway", "https://en.wikipedia.org/wiki/Ernest_Hemingway")
        + Plain(
            " once bet that he could write the shortest story that would touch anyone."
        )
    ) + Code("print('Hello world!')", "python")

    # Message shortcuts natively support text styles. They call `.to_text()` and `.to_entities()`
    # under the hood on the chain to retrieve its text and translate text styles to entities.
    await m.answer(decorations + blocks)


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

from wonda import Bot, Message, Token
from wonda.bot.rules import Command
from wonda.tools.text import Blockquote, Bold, Code, Italic, Link, Plain, Underline

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


@bot.on.message(Command("styling"))
async def styling_handler(m: Message) -> None:
    # Wonda uses custom styling builder to format text. It's easy to read and maintain,
    # and it extends as easily as the inferior styling method which uses parse modes.
    # You can decorate text with any text styles that are available today. Here's
    # an example using plain, bold, italic and underline styles.
    decorations = (
        Plain("Text. Plain and simple. ")
        + Bold("This is a bold statement. ")
        + Italic("Mama mia! ")
        + Underline("Notice me!")
    )

    # Text styling also includes Blockquote and Code blocks to help decorate long blocks
    # of text. You can put any number of entities inside these blocks, and they are
    # super easy to customize.
    blocks = Blockquote(
        Link("Ernest Hemingway", "https://en.wikipedia.org/wiki/Ernest_Hemingway")
        + Plain(
            " once bet that he could write the shortest story that would touch anyone."
        )
    ) + Code("print('Hello world!')", "python")

    # Message shortcuts natively support text styles. They call `.to_string()`
    # and `.to_entities()` under the hood on the chain to retrieve
    # its text and translate text styles to entities.
    await m.answer(decorations + blocks)


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

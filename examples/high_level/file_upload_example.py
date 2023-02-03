from wonda.bot import Bot, File, Message, Token
from wonda.bot.rules import Command

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())

# Load a file from a given path using <.from_path(...)>. Path can be
# given in the form of a string or a Path object.
SAMPLE_PHOTO = File.from_path("examples/high_level/assets/apples.webp")


@bot.on.message(Command("upload"))
async def upload_handler(msg: Message) -> None:
    # With File, you can upload any file to Telegram - be it
    # a photo, audio, video, or a document.
    await msg.ctx_api.send_photo(
        chat_id=msg.chat.id, caption="Lookin' tasty!", photo=SAMPLE_PHOTO
    )

    # While we download the image, let the user know something's brewing.
    await msg.ctx_api.send_chat_action(chat_id=msg.chat.id, action="upload_photo")

    # Download a sample image from Lorem Picsum using the HTTP client.
    content = await msg.ctx_api.http_client.request_content("https://picsum.photos/300")

    # Construct a file using <.from_bytes(...) method. It has "unnamed.bin"
    # name by default, so it's advised to give it a proper name.
    photo = File.from_bytes(content, name="random.jpg")

    # Just like that, another photo is uploaded to Telegram.
    await msg.ctx_api.send_photo(
        caption="Yay! A photo from the internet!", photo=photo, chat_id=msg.chat.id
    )

    # To enable faster uploads, use File directly. Supply it with a link to a file
    # or a file_id and Telegram will take care of the rest.
    larger_photo = File("https://picsum.photos/1000")

    # Despite the image being a lot larger,
    # it will be uploaded just as fast as the previous one!
    await msg.ctx_api.send_photo(
        caption="This one's bigger!", photo=larger_photo, chat_id=msg.chat.id
    )


# Run loop > loop.run_forever() > with tasks created in loop_wrapper before.
# The main polling task for bot is bot.run_polling()
bot.run_forever()

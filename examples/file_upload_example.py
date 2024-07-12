from wonda.bot import Bot, File, Message, Token
from wonda.bot.rules import Command

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())

# Load a file from a path using `.from_path(...)`. The path can 
# be given in the form of a string or a Path object.
SAMPLE_PHOTO = File.from_path("examples/assets/apples.jpeg")


@bot.on.message(Command("upload"))
async def upload_handler(m: Message) -> None:
    # With File, you can upload any file to Telegram - be it
    # a photo, audio, video, or a document.
    await m.ctx_api.send_photo(
        chat_id=m.chat.id, caption="Lookin' tasty!", photo=SAMPLE_PHOTO
    )

    # While we download the image, let the user know something's brewing.
    await m.ctx_api.send_chat_action(chat_id=m.chat.id, action="upload_photo")

    # Download a sample image from Lorem Picsum using the network client.
    content = await m.ctx_api.network_client.request_bytes("https://picsum.photos/300")

    # Just like that, another photo is uploaded to Telegram.
    await m.ctx_api.send_photo(
        chat_id=m.chat.id,
        caption="Yay! A photo from the internet!",
        photo=File.from_bytes(content, "random.jpg"),
    )

    # To enable faster uploads, you may not use File at all. Instead, pass a URL
    # or a file ID to the method and Telegram will take care of it.
    # Despite the image being a lot larger, it will be uploaded
    # just as fast as the previous one!
    await m.ctx_api.send_photo(
        chat_id=m.chat.id,
        caption="This one's bigger!",
        photo="https://picsum.photos/1000",
    )


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

from wonda import Bot, LoopWrapper, Message, Token

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


# Loop wrapper is a class that helps you interact with the event loop.
# It helps you run startup and shutdown tasks, and set up timers and intervals.
# A loop wrapper is created automatically when you initialize a bot and is accessible
# through `bot.loop_wrapper`. For the purpose of demostration it will be created
# manually here.
loop_wrapper = LoopWrapper()


# To set up a timer, use the `@lw.timer()` decorator. It receives
# a time interval in seconds, minutes, hours and days.
@loop_wrapper.timer(5)
async def timer_handler() -> None:
    # Timer handlers are coroutines, which means you must perform
    # non-blocking operations in them. They also accept no arguments.
    print("It's my time to shine!")


# You can also use `@lw.interval()` decorator to set up an interval coroutine.
# It will work the same way as a timer, but will be called repeatedly
# every time the interval is over until the bot is stopped.
@loop_wrapper.interval(10)
async def interval_handler() -> None:
    print("I'm here to stay!")


# A dummy handler to fill up the space
# and for you to look at. Isn't it beautiful?
@bot.on.message()
async def handler(m: Message) -> None:
    await m.answer("Hello, world!")


# To add a startup or a shutdown task, add it to a list of coroutines
# using simple append method. You can add as many tasks as you want,
# and they will be run in order of addition.
async def setup_db() -> None:
    # Here we are! Let's spin up the engines!
    # I can already hear 'em roar!
    print("Spinning up the engines...")


async def close_connection() -> None:
    # Pretend that this is a real database connection
    # and we are closing it here.
    print("Closing connection...")


# Add tasks to the list of startup and shutdown tasks.
loop_wrapper.on_startup.append(setup_db())
loop_wrapper.on_shutdown.append(close_connection())

# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.loop_wrapper = loop_wrapper
bot.run_forever()

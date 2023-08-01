from wonda import Bot, LoopWrapper, Token

loop_wrapper = LoopWrapper()

# LW is a class that helps you to interact with the event loop.
# It can help you to run startup and shutdown tasks, auto-reload your code
# and set up timers and intervals.
#
# A loop wrapper is created automatically when you initialize a bot and is accessible
# through `bot.loop_wrapper`. For some reason, it's also possible
# to create it manually.

bot = Bot(Token.from_env())


# To set up a timer, use the `@lw.timer()` decorator.
# It accepts a human-readable time intervals as arguments.
# Timer handlers are coroutines, which means you must do
# non-blocking operations in them. They also accept no arguments.
@loop_wrapper.timer(5)
async def timer_handler() -> None:
    print("It's my time to shine!")


# You can also use `@lw.interval()` decorator to set up an interval coroutine.
# It will work the same way as a timer, but will be called repeatedly
# every time the interval is over until the bot is stopped.
@loop_wrapper.interval(days=1)
async def interval_handler() -> None:
    print("I'm here to stay!")


# A dummy handler to fill up the space
# and for you to look at. Isn't it beautiful?
@bot.on.message()
async def handler(_) -> str:
    return "Hello world!"


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

# Run the bot. This function uses `.run_polling()` under the hood to start receiving updates.
# It will also run any tasks you may've added in `loop_wrapper`., which is automatically
# added when this method is called.
bot.loop_wrapper = loop_wrapper
bot.run_forever()

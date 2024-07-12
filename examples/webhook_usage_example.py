from msgspec import DecodeError, json
from starlette.applications import Starlette
from starlette.background import BackgroundTask
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route

from wonda import Bot, Message, Token
from wonda.bot.rules import Command
from wonda.types.objects import Update

# Make a bot with a token from an environment variable. In this example,
# the `.run_forever()` method of the bot interface won't be used,
# since the asynchronous loop is managed by our web server.
bot = Bot(Token.from_env())


@bot.on.message(Command("start"))
async def start_handler(m: Message) -> None:
    # Send a message so that we know everything works correctly.
    await m.answer("This message was handled using webhooks!")


async def on_startup_set_webhook() -> None:
    await bot.api.set_webhook(
        # Specify a URL to send updates to. It must be secured
        # by TLS, otherwise Telegram will reject it.
        url="",
        # Provide the secret token to ensure that requests
        # are coming from Telegram and not a harmful
        # third-party.
        secret_token="",
        # This parameter regulates how many connections to your server
        # can be open simultaneously. Use lower values to limit the load
        # on your bot, and higher values to increase your bot's throughput.
        max_connections=100,
    )


async def on_shutdown_delete_webhook() -> None:
    await bot.api.delete_webhook(
        # Use this flag to signal to Telegram whether to drop
        # updates on application shutdown.
        drop_pending_updates=False
    )


async def handle_request(req: Request) -> Response:
    # Compare secret token from request with the local token
    # to make sure the request is authorized.
    if req.headers["X-Telegram-Bot-Api-Secret-Token"] != "secret_token_here":
        # If the local secret token and request secret token aren't the same,
        # send the response code of 401, meaning that the request was
        # not authorized.
        return Response(status_code=401)

    try:
        # Assemble the body of the request and try to decode it.
        update = json.decode(await req.body(), type=Update)
    except DecodeError:
        # If the request body can't be decoded to an Update model, send
        # the response code of 400, meaning the request went bad.
        return Response(status_code=400)

    # Notify the Bot API that the request succeeded all checks. Route the update
    # in the background because it makes no sense to await it.
    return Response(
        status_code=200, background=BackgroundTask(bot.router.route, update, bot.api)
    )


# Instantiate an ASGI application. This application can be
# run via any compatible web server. We recommend using
# uvicorn as the most popular solution.
handle_request_route = Route("/", handle_request, methods=["POST"])

app = Starlette(
    routes=[handle_request_route],
    on_startup=[on_startup_set_webhook],
    on_shutdown=[on_shutdown_delete_webhook],
)

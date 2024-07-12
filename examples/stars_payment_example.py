from wonda import APIException, Bot, Message, Token
from wonda.bot.rules import Command, Function, IsSuccessfulPayment
from wonda.bot.updates import PreCheckoutQuery
from wonda.types.objects import LabeledPrice, TransactionPartnerUser

# Make a bot with a token from an environment variable.
bot = Bot(Token.from_env())


@bot.on.message(Command("invoice"))
async def xtr_invoice_handler(m: Message) -> None:
    # Replace this invoice info with your actual title,
    # description, payload and prices.
    await m.ctx_api.send_invoice(
        chat_id=m.chat.id,
        title="Support Wondergram",
        description=(
            "Your support will allow for further development "
            "and improvement of Wonda."
        ),
        payload="donation",
        currency="XTR",
        prices=[LabeledPrice("Pay", 1)],
    )


@bot.on.pre_checkout_query(
    Function[PreCheckoutQuery](lambda pq, _: pq.invoice_payload == "donation")
)
async def pre_checkout_query_handler(pq: PreCheckoutQuery) -> None:
    # Perform validation of payload inside this handler.
    await pq.answer(ok=True)


@bot.on.message(IsSuccessfulPayment())
async def successful_payment_handler(m: Message) -> None:
    # Notify the user of successful payment.
    await m.answer(
        f"Donation of {m.successful_payment.total_amount} ⭐️ received! Thank you!"
    )
    await m.ctx_api.refund_star_payment(
        m.from_.id, m.successful_payment.telegram_payment_charge_id
    )


@bot.on.message(Command("refund"))
async def refund_handler(m: Message) -> None:
    # Refund last successful transactions.
    transactions = await m.ctx_api.get_star_transactions()

    for transaction in transactions.transactions:
        if not isinstance(transaction.source, TransactionPartnerUser):
            continue

        try:
            await m.ctx_api.refund_star_payment(
                transaction.source.user.id, transaction.id
            )
        except APIException[400]:
            await m.ctx_api.send_message(
                f"Couldn't refund transaction {transaction!r}", m.from_.id
            )

    await m.ctx_api.send_message("Refunds issued", m.from_.id)


# Run the bot. This function uses `.run_polling()` under the hood to start
# receiving updates. It will also run any tasks you may've added in `loop_wrapper`.
bot.run_forever()

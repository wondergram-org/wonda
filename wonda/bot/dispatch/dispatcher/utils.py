from wonda.bot.dispatch.dispatcher import ABCDispatcher


def get_used_update_types(dispatcher: "ABCDispatcher") -> list[str]:
    update_types: list[str] = []

    for v in dispatcher.views.values():
        not_empty = v.handlers or v.middleware

        if not_empty:
            update_types.extend(v.matches)  # type: ignore

    return update_types

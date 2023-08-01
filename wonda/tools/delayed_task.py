from asyncio import sleep
from typing import Any, Callable, Coroutine

_ = Any


class DelayedTask:
    def __init__(
        self,
        seconds: int,
        func: Callable[..., Coroutine[_, _, _]],
        do_break: bool = False,
    ) -> None:
        self.func = func
        self.seconds = seconds
        self.do_break = do_break

    async def __call__(self, *args, **kwargs) -> None:
        while True:
            await sleep(self.seconds)
            await self.func(*args, **kwargs)

            if self.do_break:
                break

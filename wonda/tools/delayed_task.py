from asyncio import sleep
from typing import Any, Callable, Coroutine

_ = Any
Func = Callable[..., Coroutine[_, _, _]]


class DelayedTask:
    def __init__(self, func: Func, time: int, once: bool = False) -> None:
        self.func, self.time, self.once = func, time, once

    async def __call__(self, *args, **kwargs) -> None:
        while True:
            await sleep(self.time)
            await self.func(*args, **kwargs)

            if self.once:
                break

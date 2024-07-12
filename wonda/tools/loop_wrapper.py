from asyncio import AbstractEventLoop, get_event_loop, iscoroutine, iscoroutinefunction
from typing import Any, Callable, Coroutine

from wonda.modules import logger
from wonda.tools.delayed_task import DelayedTask

_ = Any
Task = Coroutine[_, _, _]


class LoopWrapper:
    def __init__(
        self,
        tasks: list[Task] | None = None,
        on_startup: list[Task] | None = None,
        on_shutdown: list[Task] | None = None,
    ) -> None:
        self.tasks = tasks or []
        self.on_startup = on_startup or []
        self.on_shutdown = on_shutdown or []

    def run_forever(self, loop: AbstractEventLoop | None = None) -> None:
        """
        Manages startup and shutdown tasks and makes the loop run forever.
        """

        if not len(self.tasks):
            logger.warning("Running loop without tasks")

        loop = loop or get_event_loop()

        try:
            [loop.run_until_complete(startup_task) for startup_task in self.on_startup]

            for task in self.tasks:
                loop.create_task(task)

            loop.run_forever()
        except KeyboardInterrupt:
            logger.warning("Exiting")
        finally:
            [
                loop.run_until_complete(shutdown_task)
                for shutdown_task in self.on_shutdown
            ]
            if loop.is_running():
                loop.close()

    def add_task(self, task: "Task" | Callable[..., "Task"]) -> None:
        """
        Add a task which will be run on `.run_forever()`.
        """

        if iscoroutinefunction(task) or isinstance(task, DelayedTask):
            self.tasks.append(task())
        elif iscoroutine(task):
            self.tasks.append(task)
        else:
            raise TypeError("Task should be a coroutine or coroutine function")

    def interval(
        self, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0
    ):
        """
        Repeat a task with an interval until the program stops.
        """

        seconds += minutes * 60
        seconds += hours * 60 * 60
        seconds += days * 24 * 60 * 60

        def decorator(func: Callable):
            self.add_task(DelayedTask(func, seconds))
            return func

        return decorator

    def timer(self, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0):
        """
        Run a task one time N seconds from now.
        """

        seconds += minutes * 60
        seconds += hours * 60 * 60
        seconds += days * 24 * 60 * 60

        def decorator(func: Callable):
            self.add_task(DelayedTask(func, seconds, once=True))
            return func

        return decorator

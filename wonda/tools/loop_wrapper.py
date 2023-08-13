from asyncio import AbstractEventLoop, get_event_loop, iscoroutine, iscoroutinefunction
from typing import Any, Callable, Coroutine

from wonda.tools.delayed_task import DelayedTask

_ = Any
Task = Coroutine[_, _, _]


class LoopWrapper:
    def __init__(
        self,
        *,
        tasks: list["Task"] = [],
        on_startup: list["Task"] = [],
        on_shutdown: list["Task"] = []
    ) -> None:
        self.tasks = tasks
        self.on_startup = on_startup
        self.on_shutdown = on_shutdown

    def run_forever(self, loop: AbstractEventLoop | None = None) -> None:
        """
        Runs startup tasks and makes the loop running forever
        """

        if not len(self.tasks):
            print("Running loop without tasks")

        loop = loop or get_event_loop()

        try:
            [loop.run_until_complete(startup_task) for startup_task in self.on_startup]

            for task in self.tasks:
                loop.create_task(task)

            loop.run_forever()
        except KeyboardInterrupt:
            print("Keyboard interrupt")
        finally:
            [
                loop.run_until_complete(shutdown_task)
                for shutdown_task in self.on_shutdown
            ]
            if loop.is_running():
                loop.close()

    def add_task(self, task: "Task" | Callable[..., "Task"]) -> None:
        """
        Add a task which will be run on `.run_forever()`
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
        Repeat a task with an interval until the program stops
        """

        seconds += minutes * 60
        seconds += hours * 60 * 60
        seconds += days * 24 * 60 * 60

        def decorator(func: Callable):
            self.add_task(DelayedTask(seconds, func))
            return func

        return decorator

    def timer(self, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0):
        """
        Run a task one time N seconds from now
        """

        seconds += minutes * 60
        seconds += hours * 60 * 60
        seconds += days * 24 * 60 * 60

        def decorator(func: Callable):
            self.add_task(DelayedTask(seconds, func, do_break=True))
            return func

        return decorator

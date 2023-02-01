import os
import sys
from typing import NoReturn

from wonda.modules import logger

STARTUP_DIR: str = os.getcwd()

try:
    from watchfiles import awatch as watch
except ImportError:
    watch = None


def restart() -> NoReturn:
    args = sys.argv.copy()
    args.insert(0, sys.executable)

    if sys.platform == "win32":
        args = [f'"{arg}"' for arg in args]

    os.chdir(STARTUP_DIR)
    os.execv(sys.executable, args)


async def watch_to_reload(src_dir: str) -> None:
    """
    A coroutine that restarts the app when changes
    in source code are detected.
    """

    if watch is None:
        raise SystemExit(
            "Reinstall `wonda` package with auto-reload extra "
            "before using auto reload feature"
        )

    async for _ in watch(src_dir):
        logger.info("Changes were found. Restarting...")
        restart()

from wonda import ErrorHandler

error_handler = ErrorHandler()

# You can set redirect_arguments in error handler. They
# will be passed after exception to an exception handler.
# ---
# ```
# async def f(a, b): raise RuntimeError
# async def exc_h(exc: RuntimeError, a, b): ...
# ```

# Register an error handler for this type of exception
# and all of its derivatives.
@error_handler.register_error_handler(RuntimeError)
async def exc_handler(exc: RuntimeError):
    print("Oops, error occured:", exc)


# Decorate the handler function in which an error may occur.
@error_handler.catch
async def main():
    raise RuntimeError("Dear god, I am exceptional!")


# Run an example function in the current event loop.
__import__("asyncio").get_event_loop().run_until_complete(main())

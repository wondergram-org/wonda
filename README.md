# Wonda ☁️

[//]: # (Features)
[examples]: examples/
[format text]: examples/formatting_example.py
[upload files]: examples/file_upload_example.py
[an advanced state system]: examples/use_state_dispenser.py

[//]: # (Badges)
![Version](https://img.shields.io/pypi/v/wonda?label=version&style=flat-square)
![Package downloads](https://img.shields.io/pypi/dw/wonda?label=downloads&style=flat-square)
![Supported Python versions](https://img.shields.io/pypi/pyversions/wonda?label=supported%20python%20versions&style=flat-square)

Wonda is a Telegram bot framework. It supports latest versions and features of the API. Incredibly fast and extraordinarily customizable, it gives you power to build the bot you always wanted.

## Install

```bash
pip install wonda
```

A stable version of Wonda can be installed using this command. Add `--pre` to the command to install a pre-release version.

## Features

Ever wanted to build a bot? You can do that in only 6 lines of code.

```python
from wonda import Bot, Message

bot = Bot("your-token")


@bot.on.message()
async def handler(m: Message) -> None:
    await m.answer("Hello world!")

bot.run_forever()
```

You can already [format text], [upload files], and make use of [an advanced state system] to craft complex interactions. And more features are expected to come! Check out the [examples].

## Customization

### Speed up event loop

```bash
pip install uvloop
```

Wonda supports uvloop, an event loop implementation which makes I/O [2-4x quicker](https://github.com/magicstack/uvloop#performance).

### Replace default JSON module

``` bash
pip install orjson
```

Swap out the module that is used under the hood to manipulate JSON and increase speed up to [5 times](https://github.com/ijl/orjson#performance).

## Contrubuting

The framework is not yet ready for production. If you like what you see, help us develop this amazing project! [Create an issue](https://github.com/wondergram-org/wonda/issues/new/choose) or [make a pull request](https://github.com/wondergram-org/wonda/compare).

## Copyright

- timoniq (2019-2021)
- geo-madness (2022-2023)

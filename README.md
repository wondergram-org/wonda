# Wonda 🍄

[//]: # "Features"
[examples]: examples/
[format text]: examples/text_styling_example.py
[upload files]: examples/file_upload_example.py
[an advanced state system]: examples/use_state_manager.py

[//]: # "Badges"
![Version](https://img.shields.io/pypi/v/wonda?label=version&style=flat-square)
![Package downloads](https://img.shields.io/pypi/dw/wonda?label=downloads&style=flat-square)
![Supported Python versions](https://img.shields.io/pypi/pyversions/wonda?label=supported%20python%20versions&style=flat-square)

Wonda is a Telegram bot framework. It strikes a perfect balance between simple and advanced and makes bot development a breeze. Its concepts are easy to understand and extend. And, with immediate support for latest Bot API versions, it always stays up to the standard.

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

You can already [format text], [upload files], and make use of [an advanced state system] to build complex interactions. More features are expected to come! Check out the [examples].

## Customization

Wonda ships with few dependencies by default. To customize your experience, you may want to install some extra dependencies on top.

### Speed up event loop

```bash
pip install uvloop
```

Wonda supports uvloop, an event loop implementation which makes I/O [2-4x quicker](https://github.com/magicstack/uvloop#performance).

### Replace default JSON module

```bash
pip install orjson
```

Swap out the module that is used under the hood to manipulate JSON and increase speed up to [5 times](https://github.com/ijl/orjson#performance).

### Display tracebacks in greater detail

```bash
pip install rich
```

Check out [rich](https://github.com/textualize/rich), a library which provides amazing rich text capabilities for your logs.

## Contrubuting

This framework is a robust solution for what it's worth, but the API may be unstable for a while. That means it's not yet ready for production use.

So, if you like our work, help us develop this amazing project! Here are some ways you can help.

### With code

Contributions are welcome! [File a ticket](https://github.com/wondergram-org/wonda/issues) if you have something to say about the state of the framework.

### With finances

There are a couple options available for monetary help. Click [Sponsor](https://boosty.to/geo_madness) to see them. Thank you!

## License

This project exists thanks to the amazing work done by timoniq. Code is licensed under [MIT](LICENSE). Copyright (c) 2022-2024 kikimaradoni

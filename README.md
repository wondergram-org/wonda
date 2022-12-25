# Wonda ✨

[//]: # (Examples)
[examples]: examples/high_level
[text formatting]: examples/high_level/formatting_example.py
[middleware]: examples/high_level/setup_middleware.py
[file uploading]: examples/high_level/file_upload_example.py
[blueprints]: examples/high_level/load_blueprints.py
[FSM]: examples/high_level/use_state_dispenser.py

[//]: # (Badges)
![Version](https://img.shields.io/pypi/v/wonda?label=version&style=flat-square)
![Package downloads](https://img.shields.io/pypi/dw/wonda?label=downloads&style=flat-square)
![Supported Python versions](https://img.shields.io/pypi/pyversions/wonda?label=supported%20python%20versions&style=flat-square)

## Why

Wonda can help you build bots using simple tools without losing performance. It has all batteries included: [text formatting], [file uploading], [blueprints], [middleware] and [FSM] are usable right away.

## Versions

### Stable or pre-release

To install a stable version of Wonda, enter this command in your terminal:

```shell script
pip install -U wonda
```

If you decide to go beta, use the same command with `--pre` option or update from dev branch .zip [archive](https://github.com/wondergram-org/wonda/archive/refs/heads/dev.zip).

### Performance

You can make Wonda perform even better by installing power-ups. They're optional, but highly recommended.

```shell script
pip install --force wonda[power-ups]
```

To see the full list of packages, refer to our [project file](pyproject.toml).

## Guide

It's easy to build a bot with Wonda — it's ready in *six* lines of code. Extending it is no problem too.

```python
from wonda import Bot

bot = Bot("your-token")


@bot.on.message()
async def handler(_) -> str:
    return "Hello world!"

bot.run_forever()
```

With Wonda, it's possible to achieve this much with so little code. To get started, check out our [examples].

## Contributing

Wonda is a work in progress and a lot of stuff is expected to change! It's the right time for your input.

If you want to report a bug or suggest a feature, [create an issue](https://github.com/wondergram-org/wonda/issues/new/choose). To ask a question, please use [discussions](https://github.com/wondergram-org/wonda/discussions). Big thanks!

## License

This project is MIT licensed. Based upon hard work of maintainers and contributors of [VKBottle](https://github.com/vkbottle/vkbottle).

Copyright © timoniq (2019-2021), feeeek (2022), geo-madness (2022)

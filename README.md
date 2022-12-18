# Wonda ✨

[//]: # (Links to examples)
[text formatting]: examples/high_level/formatting_example.py
[middleware]: examples/high_level/setup_middleware.py
[file uploading]: examples/high_level/file_upload_example.py
[blueprints]: examples/high_level/load_blueprints.py
[FSM]: examples/high_level/use_state_dispenser.py
[awesome examples]: examples/high_level

![Version](https://img.shields.io/pypi/v/wonda?label=version&style=flat-square)
![Package downloads](https://img.shields.io/pypi/dw/wonda?label=downloads&style=flat-square)
![Supported Python versions](https://img.shields.io/pypi/pyversions/wonda?label=supported%20python%20versions&style=flat-square)

## Why

Wonda empowers you to build powerful bots using simple extensible tools while not sacrifing any performance. It has all batteries included: [text formatting], [file uploading], [blueprints], [middleware] and [FSM] are all built-in.

## Install

To install stable version, use

```shell script
pip install -U wonda
```

If you decide to go beta, use the same command with `--pre` option or update from dev branch .zip [archive](https://github.com/wondergram-org/wonda/archive/refs/heads/dev.zip).

You can make Wonda perform even better by installing power-ups. They're optional, but highly recommended.

```shell script
pip install --force wonda[power-ups]
```

To see the full list of packages, refer to our [project file](pyproject.toml).

## Usage

It's easy to build an echo bot with Wonda — it's ready in *six* lines of code. And expanding it further is a piece of cake too.

```python
from wonda import Bot

bot = Bot("your-token")


@bot.on.message()
async def handler(_) -> str:
    return "Hello world!"

bot.run_forever()
```

Isn't it beautiful how little code is needed to achieve something this big? To get started on Wonda, check out our [awesome examples].

## License

This project is MIT licensed. Big thanks to maintainers and contributors of [vkbottle](https://github.com/vkbottle/vkbottle) upon which it is built!

© timoniq (2019-2021), feeeek (2022), exthrempty (2022)

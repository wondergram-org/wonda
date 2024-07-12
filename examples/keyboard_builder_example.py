from wonda.tools.keyboard import Button, Contact, Location, ReplyKeyboardBuilder
from wonda.types.objects import KeyboardButton, ReplyKeyboardMarkup

# There are two ways of constructing a keyboard in Wonda. The first is to simply
# describe its schema using API objects.
KEYBOARD_VIA_SCHEMA = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton("Send my phone number", request_contact=True),
            KeyboardButton("Share a location", request_location=True),
        ],
        [KeyboardButton("Back to menu")],
    ],
)

# Using keyboard builder is way simpler. You can add buttons and make new rows
# on the keyboard using methods like `.add()` and `.row()`, make adjustments
# to its width via `.adjust()` or even merge keyboards together using `.merge()`.
KEYBOARD_VIA_BUILDER = (
    ReplyKeyboardBuilder(resize_keyboard=True)
    .add(Contact("Send my phone number"))
    .add(Location("Share a location"))
    .row()
    .add(Button("Back to menu"))
    .build()
)

# Check that the two keyboards are the same.
assert KEYBOARD_VIA_SCHEMA == KEYBOARD_VIA_BUILDER

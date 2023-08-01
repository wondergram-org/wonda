from wonda.tools.keyboard import Button, Contact, Location, ReplyKeyboardBuilder

# The simplest way of generating keyboard is using non-builder interface.
# Use <.add(Button(...))> to add button to the last row, then <.row()> to add row.
KEYBOARD_STANDARD = ReplyKeyboardBuilder(resize_keyboard=True)
KEYBOARD_STANDARD.add(Contact("Send my phone number"))
KEYBOARD_STANDARD.add(Location("Share a location"))
KEYBOARD_STANDARD.row()
KEYBOARD_STANDARD.add(Button("Back to menu"))

# <.add(...)> and <.row()> methods return the instance of Keyboard,
# so you can use it as a builder
KEYBOARD_WITH_BUILDER = (
    ReplyKeyboardBuilder(resize_keyboard=True)
    .add(Contact("Send my phone number"))
    .add(Location("Share a location"))
    .row()
    .add(Button("Back to menu"))
)

# Check that the two keyboards are the same.
assert KEYBOARD_STANDARD.build() == KEYBOARD_WITH_BUILDER.build()

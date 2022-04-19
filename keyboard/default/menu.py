from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Barbi"),
            KeyboardButton(text="Riley's first date"),
        ],
        [
            KeyboardButton(text="Sponge Bob Square Pants"),
            KeyboardButton(text="Bratz"),
        ],
        [
            KeyboardButton(text="Smeshariki"),
        ],
    ],
    resize_keyboard=True
)
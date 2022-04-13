#keyboard.defalt
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Real Madrid"),
            KeyboardButton(text="Barcelona")
        ],
        [
            KeyboardButton(text="Chelsea"),
            KeyboardButton(text="Manchester United")
        ],
    ],
    resize_keyboard=True
)
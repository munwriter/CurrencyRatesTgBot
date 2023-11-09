from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='USD $'),
            KeyboardButton(text='EUR €'),
            KeyboardButton(text='RUB ₽'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Choose currency',
)

main_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Current major exchange rates'),
        ],
    ],
    resize_keyboard=True
)

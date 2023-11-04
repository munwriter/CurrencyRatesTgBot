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

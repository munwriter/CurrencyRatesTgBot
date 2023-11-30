from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

currencies_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Show available currencies", callback_data="currencies_list"
            ),
        ]
    ]
)


menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="View current settings")],
        [KeyboardButton(text="About")],
    ],
    resize_keyboard=True
)

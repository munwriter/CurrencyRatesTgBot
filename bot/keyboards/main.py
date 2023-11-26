from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

buttons = buttons = [
        [
            InlineKeyboardButton(text="Show available currencies", callback_data="currencies_list"),
        ]
    ]
currencies_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
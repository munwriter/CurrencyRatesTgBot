from aiogram import Router, F
from aiogram.types import Message

from bot.misc.literals import *
from services.db.main import DataBase


menu_router = Router()


@menu_router.message(F.text == 'View current settings')
async def view_user_settings(message: Message) -> None:
    user_cfg_data = DataBase().get_user_settings(message.from_user.id)
    rounding_idx, source_currency, req_currency = (
        user_cfg_data[1],
        user_cfg_data[2],
        user_cfg_data[3],
    )
    await message.answer(
        USER_SETTINGS_MESSAGE.format(
            rounding_idx=rounding_idx, source_cur=source_currency, req_cur=req_currency
        )
    )


@menu_router.message(F.text == 'About')
async def about(message: Message) -> None:
    await message.answer('https://github.com/munwriter/CurrencyRatesTgBot')

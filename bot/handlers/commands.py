from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.misc.constants import *
from bot.misc.literals import *
from services.db.main import DataBase
from services.webQueries.main import request_currencies

commands_router = Router()


@commands_router.message(Command('live'))
async def live_currencies(message: Message) -> None:
    db = DataBase().get_user_settings(message.from_user.id)
    source_curr, req_curr = db[2], db[3]
    response_data = await request_currencies(
        'live', {'source': source_curr, 'currencies': req_curr}, message.from_user.id
    )
    await message.answer(response_data)


@commands_router.message(Command('list'))
async def currencies_list(message: Message) -> None:
    await message.answer(CURRENCIES_MESSAGE)

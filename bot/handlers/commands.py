from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.misc.literals import *
from bot.misc.constants import *
from bot.keyboards import main as kb
from services.webQueries.main import request_currencies


commands_router = Router()


@commands_router.message(Command(commands=['live']))
async def live_currencies(message: Message) -> None:
    res = await request_currencies('live', {'source': 'RUB', 'currencies': 'USD,EUR,SLL,SYP,PHP'})
    await message.answer(res)


@commands_router.message(Command(commands=['list']))
async def currencies_list(message: Message) -> None:
    await message.answer(CURRENCIES_MESSAGE)

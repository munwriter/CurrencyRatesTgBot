from decimal import Decimal, InvalidOperation

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.misc.literals import *
from bot.misc.constants import *
from bot.states.main import Convert
from services.main import request_currencies


convert_router = Router()


@convert_router.message(Command(commands=['convert']))
async def convert_currencies(message: Message, state: FSMContext) -> None:
    await state.set_state(Convert.amount)
    await message.answer('Enter the amount of currency you would like to convert.')


@convert_router.message(Convert.amount)
async def convert_currencies_amount(message: Message, state: FSMContext) -> None:
    try:
        amount = Decimal(message.text)
    except (InvalidOperation, TypeError):
        await message.answer('Pleas enter valid amount!')
    else:
        await state.update_data(amount=amount)
        await state.set_state(Convert.from_)
        await message.answer(ENTER_CURRENCY_MESSAGE.format(direction='from'))


@convert_router.message(Convert.from_)
async def convert_currencies_from(message: Message, state: FSMContext) -> None:
    if isinstance(message.text, str) and message.text.upper() in CURRENCIES:
        from_ = message.text.upper()
        await state.update_data(from_=from_)
        await state.set_state(Convert.to)
        await message.answer(ENTER_CURRENCY_MESSAGE.format(direction='to'))
    else:
        await message.answer(INVALID_CURRENCY)


@convert_router.message(Convert.to)
async def convert_currencies_from(message: Message, state: FSMContext) -> None:
    if isinstance(message.text, str) and message.text.upper() in CURRENCIES:
        to = message.text.upper()
        await state.update_data(to=to)
        response_data = await state.get_data()
        result = await request_currencies('convert', params={'to': response_data['to'],
                                                             'from': response_data['from_'],
                                                             'amount': response_data['amount'],
                                                             }
                                          )
        await message.answer(result)
    else:
        await message.answer(INVALID_CURRENCY)
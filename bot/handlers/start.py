"""The starting handlers start the state process to register the basic currency config"""
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards import main as kb
from bot.misc.constants import *
from bot.misc.literals import *
from bot.states.main import Currencies
from bot.utils.currencies_validator import validate_currencies
from services.db.main import DataBase

start_router = Router()


@start_router.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    await state.set_state(Currencies.source_currency)
    await message.answer(
        GREETINGS_MESSAGE.format(name=message.from_user.full_name),
        reply_markup=kb.start_keyboard,
    )
    await message.answer(CURRENCIES_MESSAGE)


@start_router.message(Currencies.source_currency)
async def complete_currencies_cfg(message: Message, state: FSMContext) -> None:
    """Validate user message(correct format and content) and set next
    state in positive case.
    """
    if validate_currencies(message.text, single=True):
        await state.update_data(source_currency=message.text.upper())
        await state.set_state(Currencies.required_currencies)
        await message.answer(CURRENCY_MESSAGE.format(option='required',
                                                     singular_or_plural='ies'))
    else:
        await message.answer(INVALID_CURRENCY)


@start_router.message(Currencies.required_currencies)
async def complete_currencies_cfg(message: Message, state: FSMContext) -> None:
    """Validate user message(correct format and content) and if all good
    checks the message for the eq with {source_currency_stage}.
    """
    if validate_currencies(message.text):
        await state.update_data(required_currencies=message.text.upper())
        await state.set_state(Currencies.rounding_idx)
        await message.answer(
            'Finally enter the rounding index(number of nums after comma)'
        )
    else:
        await message.answer(INVALID_CURRENCY)


@start_router.message(Currencies.rounding_idx)
async def complete_currencies_cfg(message: Message, state: FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(rounding_idx=int(message.text))
        await message.answer('<b>Excellent! Basic setup is finished.</b>')
        data = await state.get_data()
        await state.clear()
        db = DataBase().cfg_user_settings(
            message.from_user.id,
            data['rounding_idx'],
            data['source_currency'],
            data['required_currencies'],
        )
    else:
        await message.answer('Please enter valid index!')

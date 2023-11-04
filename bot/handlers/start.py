"""The starting handlers start the state process to register the basic currency config"""
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.misc.textConstants import *
from bot.states.cfgCurrencies import Currencies
from bot.keyboards import main as kb


start_router = Router()
currencies_collection = ('USD $', 'EUR €', 'RUB ₽')


@start_router.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:
    await state.set_state(Currencies.source_currency)
    await message.answer(GREETINGS_MESSAGE.format(name=message.from_user.full_name), reply_markup=kb.start_keyboard)


@start_router.message(Currencies.source_currency)
async def complete_currencies_cfg(message: Message, state: FSMContext) -> None:
    """Validate user message(correct format and content) and set next 
    state in positive case.
    """

    if isinstance(message.text, str) and message.text in currencies_collection:
        global source_currency_stage
        source_currency_stage = message.text
        await state.update_data(source_currency=message.text)
        await state.set_state(Currencies.required_currency)
        await message.answer('Now set required currency.')
    else:
        await message.answer('Please enter valid currency!')


@start_router.message(Currencies.required_currency)
async def complete_currencies_cfg(message: Message, state: FSMContext) -> None:
    """Validate user message(correct format and content) and if all good
    checks the message for the eq with {source_currency_stage}.
    """

    if isinstance(message.text, str) and message.text in currencies_collection:
        if message.text == source_currency_stage:
            await message.answer('Source currency and required currency shouldn`t be equal!')
        else:
            await state.update_data(required_currency=message.text)
            await state.clear()
            await message.answer('<b>Excellent! Basic setup is finished.</b>')
    else:
        await message.answer('Please enter valid currency!')

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile, Message
from matplotlib import pyplot as plt

from bot.misc.constants import *
from bot.misc.literals import *
from bot.states.main import TimeFrame
from bot.utils.currencies_validator import validate_currencies
from bot.utils.date_validators import validate_date, validate_dates_range
from services.graphics.main import Graphic
from services.webQueries.main import request_currencies

time_frame_router = Router()


@time_frame_router.message(Command('timeframe'))
async def timeframe(message: Message, state: FSMContext) -> None:
    await state.set_state(TimeFrame.start_date)
    await message.answer(ENTER_DATE_MESSAGE.format(option='start'))


@time_frame_router.message(TimeFrame.start_date)
async def start_date(message: Message, state: FSMContext) -> None:
    if isinstance(message.text, str) and validate_date(message.text):
        await state.update_data(start_date=message.text)
        await state.set_state(TimeFrame.end_date)
        await message.answer(ENTER_DATE_MESSAGE.format(option='end'))
    else:
        await message.answer(INVALID_DATE)


@time_frame_router.message(TimeFrame.end_date)
async def end_date(message: Message, state: FSMContext) -> None:
    start_date = await state.get_data()
    if (
        isinstance(message.text, str)
        and validate_date(message.text)
        and validate_dates_range(start_date['start_date'], message.text)
    ):
        await state.update_data(end_date=message.text)
        await state.set_state(TimeFrame.source_currency)
        await message.answer(
            CURRENCY_MESSAGE.format(option='source', singular_or_plural='y')
        )
    else:
        await message.answer(INVALID_DATE)


@time_frame_router.message(TimeFrame.source_currency)
async def source_cur(message: Message, state: FSMContext) -> None:
    if validate_currencies(message.text, single=True):
        await state.update_data(source_currency=message.text.upper())
        await state.set_state(TimeFrame.required_currency)
        await message.answer(
            CURRENCY_MESSAGE.format(option='required', singular_or_plural='ies')
        )
    else:
        await message.answer(INVALID_CURRENCY)


@time_frame_router.message(TimeFrame.required_currency)
async def req_cur(message: Message, state: FSMContext) -> None:
    if validate_currencies(message.text):
        formatted_currencies = ','.join(message.text.upper().split())
        await state.update_data(required_currency=formatted_currencies)
        query_parameters = await state.get_data()
        await state.clear()
        query_data = TIMEFRAME_MESSAGE.format(
            source_currency=query_parameters['source_currency'],
            required_currencies=query_parameters['required_currency'],
            start_date=query_parameters['start_date'],
            end_date=query_parameters['end_date'],
        )
        response_data = await request_currencies(
            'timeframe',
            {
                'end_date': query_parameters['end_date'],
                'start_date': query_parameters['start_date'],
                'currencies': query_parameters['required_currency'],
                'source': query_parameters['source_currency'],
            },
        )
        if isinstance(response_data, str):
            await message.answer(response_data)
        else:
            await message.answer(query_data)
            graphic = Graphic(plt).draw_graphics(
                response_data[0], response_data[1], response_data[2]
            )
            graphic.config_graphic('Dates', 'Currencies value', 'Timeframe')
            graphic = graphic.graphic_pic_to_bytes()
            await message.answer_photo(BufferedInputFile(graphic, "currencies-graphic"))
    else:
        await message.answer(INVALID_CURRENCY)

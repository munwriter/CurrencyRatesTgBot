from aiogram.fsm.state import StatesGroup, State


class Currencies(StatesGroup):
    source_currency = State()
    required_currency = State()
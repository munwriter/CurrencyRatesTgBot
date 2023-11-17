from aiogram.fsm.state import StatesGroup, State


class Currencies(StatesGroup):
    source_currency = State()
    required_currency = State()


class Convert(StatesGroup):
    amount = State()
    from_ = State()
    to = State()


class TimeFrame(StatesGroup):
    start_date = State()
    end_date = State()
    source_currency = State()
    required_currency = State()

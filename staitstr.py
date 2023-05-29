from aiogram.dispatcher.filters.state import State,StatesGroup

class TranslaterState(StatesGroup):
    til = State()
    tarjima = State()
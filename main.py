import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from config import BOT_TOKEN
from buttons import main_markup
from staitstr import TranslaterState
from googletrans import Translator


logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_tr(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user} botga hush kelibsiz\nKerakli bolimni tanglang!", reply_markup=main_markup)
    await TranslaterState().til.set()

  
@dp.message_handler(state=TranslaterState.til)
async def til_tanlov(message: types.Message, state: FSMContext):
    til = message.text
    await state.update_data( {"til": til}, )
    await message.answer(f"Tarjima qilinuvchi matnni kiriting:")
    await TranslaterState.next()

@dp.message_handler(state=TranslaterState.tarjima)
async def translate_text(message: types.Message, state: FSMContext):
    matn = message.text
    data = await state.get_data()
    till = data.get("til")
    tarjimon = Translator()
    if till == "🇺🇿 Uzb - 🇬🇧 Eng":
        tarjima = tarjimon.translate(matn, dest="en")
        await message.answer(tarjima.text, reply_markup=main_markup)
    elif till =="🇬🇧 Eng - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(matn, dest="uz")
        await message.answer(tarjima.text, reply_markup=main_markup)
    elif till == "🇺🇿 Uzb - 🇷🇺 Rus":
        tarjima = tarjimon.translate(matn, dest="ru")
        await message.answer(tarjima.text, reply_markup=main_markup)
    elif till == "🇷🇺 Rus - 🇺🇿 Uzb":
        tarjima = tarjimon.translate(matn, dest="uz")
        await message.answer(tarjima.text, reply_markup=main_markup)
    await TranslaterState.til.set()
    
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
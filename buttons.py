from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

main_markup = ReplyKeyboardMarkup(resize_keyboard=True,
    one_time_keyboard=True)
main_markup.row(KeyboardButton(text="🇺🇿 Uzb - 🇬🇧 Eng"),KeyboardButton(text="🇺🇿 Uzb - 🇷🇺 Rus"))
main_markup.row( KeyboardButton(text="🇷🇺 Rus - 🇺🇿 Uzb"),KeyboardButton(text="🇬🇧 Eng - 🇺🇿 Uzb"))
 
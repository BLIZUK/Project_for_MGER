#  Подключение библиотек
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


#  Создание 5 клавиш
def help_buttons_DEF() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Предложить идею"),
        types.KeyboardButton(text="Мероприятия")
    )
    return builder.as_markup(resize_keyboard=True)

#  Подключение библиотек
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


#  Создание 5 клавиш
def help_buttons() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="/test1", ),
        types.KeyboardButton(text="/test2")
    )
    # builder.row(
    #   types.KeyboardButton(text=locale_txt, requests_loation=True)
    # )
    builder.row(
        types.KeyboardButton(text="/ID"),
        types.KeyboardButton(text="/test3"),
    )
    builder.row(
        types.KeyboardButton(text="/off")
    )
    return builder.as_markup(resize_keyboard=True)

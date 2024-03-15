from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def button_send() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Рассылка"),
    )
    return builder.as_markup(resize_keyboard=True)


def button_choose() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Рассылка для доверенных лиц"),
        types.KeyboardButton(text="Общая рассылка")
    )
    return builder.as_markup(resize_keyboard=True)


def buttons_admin_off() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Off"),
    )
    return builder.as_markup(resize_keyboard=True)

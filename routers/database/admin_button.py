from aiogram import types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def button_send() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Рассылка"),
        types.KeyboardButton(text="Активисты"),
        types.KeyboardButton(text="Мероприятия")
    )
    return builder.as_markup(resize_keyboard=True)


def button_choose_send() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Рассылка для доверенных лиц"),
        types.KeyboardButton(text="Общая рассылка"),
    )
    return builder.as_markup(resize_keyboard=True)


def buttons_admin_off() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Off"),
    )
    return builder.as_markup(resize_keyboard=True)

# Нужно сделать resizes всех клавиатур, Уолтер
def button_for_event() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Создать мероприятие"),
        types.KeyboardButton(text="Прошедшие мероприятия"),
        types.KeyboardButton(text="Предстоящие мероприятия")
    )
    return builder.as_markup(resize_keyboard=True)


def buttom_admin_edit() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Имя"),
        types.KeyboardButton(text="Фамилия"),
        types.KeyboardButton(text="Отчество"),
        types.KeyboardButton(text="Дата рождения"),
        types.KeyboardButton(text="Первичное отделение"),
        types.KeyboardButton(text="Фото"),
        types.KeyboardButton(text="Телефон")
    )
    return builder.as_markup(resize_keyboard=True)



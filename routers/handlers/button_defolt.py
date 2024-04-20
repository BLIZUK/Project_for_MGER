#  Подключение библиотек
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


#  Включение клавиатуры для обычных пользователей, не имеющих прав администратора
#  Используются риплай клавиши (ReplayKeyboard)


def help_buttons_def() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="Предложить идею"),
        types.KeyboardButton(text="Мероприятия")
    )
    return builder.as_markup(resize_keyboard=True)


#  Прокерка рабоыт инлайн кнопок

def check_id_inline_button() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="Посмотреть мой id", callback_data=f"Посмотреть мой id")
    )
    return builder.as_markup()

#  Подключение библиотек
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums.parse_mode import ParseMode
from .admin_button import buttons_admin_off
#  Импортируем кнопки из файла button_defolt.py
#  Импортируем текст из файла text.py

from ..handlers.text import ADMIN, ID_peopl, ADMINs, SPAm

router = Router(name=__name__)


@router.message(Command("Рассылка", "р", "Р", "P", "p"))
async def cmd_test4(message: Message, bot: Bot):
    if message.from_user.id == ADMINs:
        await message.reply(SPAm)
        @router.message(F.text)
        async def cmd_test4_2_1(message: Message):
            if message.from_user.id == ADMINs:
                await message.reply("Введите 'off' для прекращения рассылки", reply_markup=buttons_admin_off())
                mailing = message.text
                for key in (ID_peopl.keys()):
                    await bot.send_message(ID_peopl[key], mailing + f"\nby <b>{message.from_user.full_name}</b>", disable_notification=True, parse_mode=ParseMode.HTML )
    else:
        await message.reply("У вас нет прав для такой функции!")

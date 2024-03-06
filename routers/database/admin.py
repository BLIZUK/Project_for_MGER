#  Подключение библиотек
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums.parse_mode import ParseMode
import sys
#  Импортируем кнопки из файла button.py
#  Импортируем текст из файла text.py

from aiogram import Router

from ..handlers.text import ADMIN, ID_peopl, test4_txt, ADMINs

router = Router(name=__name__)


@router.message(Command("test4"))
async def cmd_test4(message: Message, bot: Bot):
    if message.from_user.id == ADMINs:
        await message.answer("Выберите режим рассылки:")

        @router.message(F.text.lower() == "автомат")
        async def cmd_test4_1(message: Message):
            # if F.text.lower() == "авто":
            for key in (ID_peopl.keys()):
                await bot.send_message(ID_peopl[key], test4_txt, disable_notification=True,
                                       reply_markup=ReplyKeyboardRemove())
            # elif message.text.lower() == "ручное":

        @router.message(F.text.lower() == "ручное")
        async def cmd_test4_2(message: Message):
            await message.reply("Введите нужное сообщение для рассылки: ")

            @router.message(F.text)
            async def cmd_test4_2_1(message: Message):
                mailing = message.text
                for key in (ID_peopl.keys()):
                    await bot.send_message(ID_peopl[key], mailing, disable_notification=True)
    else:
        await message.reply("У вас нет прав для такой функции!")

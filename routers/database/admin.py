#  Подключение библиотек
from aiogram import Router, F, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums.parse_mode import ParseMode
from aiogram.methods.delete_message import DeleteMessage
from .admin_button import buttons_admin_off
#  Импортируем кнопки из файла button_defolt.py
#  Импортируем текст из файла text.py

from ..handlers.text import ADMIN, ID_peopl, ADMINs, SPAm, help_end_txt

router = Router(name=__name__)


@router.message(F.text == "Рассылка")
async def cmd_test4(message: Message, bot: Bot):
    if message.from_user.id == ADMINs:
        await message.reply(SPAm)
        msg = await message.reply("Введите 'off' для прекращения рассылки", reply_markup=buttons_admin_off())
        @router.message(F.text)
        async def cmd_test4_2_1(message: Message):
                mailing = message.text
                if mailing == "Off":
                    await message.reply(help_end_txt, reply_markup=ReplyKeyboardRemove())
                    await bot(DeleteMessage(chat_id=msg.chat.id, message_id=msg.message_id))
                else:
                    for key in (ID_peopl.keys()):
                        await bot.send_message(ID_peopl[key], mailing + f"\nby <b>{message.from_user.full_name}</b>",
                                                   disable_notification=True, parse_mode=ParseMode.HTML)
    else:
        await message.reply("У вас нет прав для такой функции!")

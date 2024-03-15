#  Подключение библиотек
from aiogram import Router, F, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums.parse_mode import ParseMode
from aiogram.methods.delete_message import DeleteMessage
from .admin_button import buttons_admin_off, button_choose
#  Импортируем кнопки из файла button_defolt.py
#  Импортируем текст из файла text.py

from ..handlers.text import ADMIN, ID_all_peopl, ID_glad_people, ADMINs, SPAm, help_end_txt

router = Router(name=__name__)


@router.message(F.text == "Рассылка")
async def cmd_send_choose(message: Message, bot: Bot):
    if message.from_user.id == ADMINs:
        await message.answer("Выберете режим рассылки: ", reply_markup=button_choose())
    else:
        await message.reply("У вас нет прав для такой функции!")


@router.message(F.text == "Общая рассылка")
async def cmd_send_all(message: Message, bot: Bot):
    if message.from_user.id == ADMINs:
        msg = await message.reply(SPAm)
        @router.message(F.text)
        async def cmd_send_all_R(message: Message, bot: Bot):
            mailing = message.text
            if mailing == "Off":
                await message.reply(help_end_txt, reply_markup=ReplyKeyboardRemove())
                await bot(DeleteMessage(chat_id=msg.chat.id, message_id=msg.message_id))
            else:
                for key in (ID_all_peopl.keys()):
                    await bot.send_message(ID_all_peopl[key], mailing + f"\nby <b>{message.from_user.full_name}</b>",
                                           disable_notification=True, parse_mode=ParseMode.HTML)


@router.message(F.text == "Рассылка для доверенных лиц")
async def cmd_send_fav(message: Message, bot: Bot):
    if message.from_user.id == ADMINs:
        msg = await message.reply(SPAm)

        @router.message(F.text)
        async def cmd_send_fav_R(message: Message, bot: Bot):
            mailing = message.text
            if mailing == "Off":
                await message.reply(help_end_txt, reply_markup=ReplyKeyboardRemove())
                await bot(DeleteMessage(chat_id=msg.chat.id, message_id=msg.message_id))
            else:
                for key in (ID_glad_people.keys()):
                    await bot.send_message(ID_glad_people[key], mailing + f"\nby <b>{message.from_user.full_name}</b>",
                                           disable_notification=True, parse_mode=ParseMode.HTML)

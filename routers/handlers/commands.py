#  Подключение библиотек
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.enums.parse_mode import ParseMode

#  Импортируем кнопки из файла button.py
from .button import help_buttons
#  Импортируем текст из файла text.py
from .text import (welcome, help_txt, help_end_txt, ID_peopl, test1_txt,
                   test2_txt, test3_txt, ADMIN, welcome_for_manuall,
                   help_txt_manuall)

router = Router(name=__name__)


# Включение чата и вызов приветственного ответа
@router.message(Command("start"))
async def cmd_start(message: Message):
    if message.from_user.id == ADMIN:
        await message.answer(f"<b>{message.from_user.full_name}</b>," + welcome + f"\nТвой ID: {message.from_user.id}"
                                                                              f"", parse_mode=ParseMode.HTML)
    else:
        await message.answer(welcome_for_manuall)


#  Вызывает окно с командами
@router.message(Command("help"))
async def cmd_help(message: Message):
    if message.from_user.id == ADMIN:
        await message.answer(help_txt, reply_markup=help_buttons())
    else:
        await message.answer(help_txt_manuall)


#  Отвечает на сообщение
@router.message(F.text.lower() == "event" or "Event")
async def cmd_test1(message: Message):
    await message.answer(test1_txt)


#  Пишет сообщение
@router.message(F.text.lower() == "send" or "Send")
async def cmd_test2(message: Message):
    await message.reply(test2_txt)


#  Отправление ID юзера
@router.message(F.text.lower() == "мой id")
async def cmd_test_id(message: Message):
    await message.reply(f"Твой ID: {message.from_user.id}")


@router.message(Command("off"))
async def cmd_test4(message: Message):
    await message.reply(help_end_txt, reply_markup=ReplyKeyboardRemove())


#  Проверка на отправку сообщения по ID чата с выбором человека
@router.message(Command("test3"))
async def cmd_test3(massage: Message, bot: Bot):
    await massage.reply(test3_txt, reply_markup=ReplyKeyboardRemove())

    @router.message(F.text.lower() == "андрей")
    async def send_emoji_id(message: Message):
        await bot.send_dice(ID_peopl["андрей"], emoji=DiceEmoji.DICE)

    @router.message(F.text.lower() == "ваня")
    async def send_emoji_id(message: Message):
        await bot.send_dice(ID_peopl["ваня"], emoji=DiceEmoji.SLOT_MACHINE)

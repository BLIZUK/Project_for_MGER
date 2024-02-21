from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums.dice_emoji import DiceEmoji


#  Импортируем кнопки из файла button
from .button import get_yes_or_no


router = Router(name=__name__)


# Сервисные команды
@router.message(Command("start"))   # [1] --> [2]
async def cmd_start(message: Message):
    await message.answer("Стартуем?", reply_markup=get_yes_or_no())


# Отвечает на сообщение
@router.message(Command("test1"))
async def cmd_test1(message: Message):
    await message.reply("test1")


# Пишет сообщение
@router.message(Command("test2"))
async def cmd_test2(message: Message):
    await message.answer("test2")


# Отправление ID юзера
@router.message(Command("ID"))
async def cmd_test_id(message: Message):
    await message.reply(f"Твой ID: {message.from_user.id}")


# Проверка на отправку сообщения по ID чата
@router.message(Command("test3"))
async def cmd_test3(massage: Message, bot: Bot):
    await bot.send_dice(866669644, emoji=DiceEmoji.DICE)


# [2]:  Проверка на ввод сообщений
@router.message(F.text.lower() == "да")
async def answer_yes(message: Message):
    await message.answer("Здорово!", reply_markup=ReplyKeyboardRemove())


@router.message(F.text.lower() == "нет")
async def answer_no(message: Message):
    await message.answer("Никому это не интересно, Стартуем!", reply_markup=ReplyKeyboardRemove())

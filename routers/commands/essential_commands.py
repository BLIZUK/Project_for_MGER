from aiogram import Router, types
from aiogram.filters.command import Command
from text import text_help

router = Router(name=__name__)


#  Старт бота
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.reply(text=text_help)
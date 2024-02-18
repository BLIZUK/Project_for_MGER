from aiogram import Router, types, Bot
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji


router = Router(name=__name__)

@router.message(Command("test1"))
async def cmd_test1(message: types.Message):
        await message.reply("test1")

    # Пишет сообщение
@router.message(Command("test2"))
async def cmd_test2(message: types.Message):
        await message.answer("test2")

@router.message(Command("ID"))
async def cmd_test_id(message: types.Message):
        await message.reply(f"Твой ID: {message.from_user.id}")

    # Проверка на отправку сообщения по ID чата, можно аргументы пихать дохуя ыыыыыыыыыыы
@router.message(Command("test3"))
async def cmd_test3(message: types.Message, bot: Bot):
        await bot.send_dice(500679707, emoji=DiceEmoji.DICE, disable_notification=True)
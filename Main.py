import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji

import config


# from handlers import router


async def main():
    #  Токен берем из другого файла
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

    # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
    # Но явное лучше неявного =]
    dp = Dispatcher(storage=MemoryStorage())

    #  Старт бота
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("Hello!")

    # Отвечает на сообщение
    @dp.message(Command("test1"))
    async def cmd_test1(message: types.Message):
        await message.reply("test1")

    # Пишет сообщение
    @dp.message(Command("test2"))
    async def cmd_test2(message: types.Message):
        await message.answer("test2")

    @dp.message(Command("ID"))
    async def cmd_test_id(message: types.Message):
        await message.reply(f"Твой ID: {message.from_user.id}")

    # Проверка на отправку сообщения по ID чата, можно аргументы пихать дохуя ыыыыыыыыыыы
    @dp.message(Command("test3"))
    async def cmd_test3(massage: types.Message, bot: Bot):
        await bot.send_dice(500679707, emoji=DiceEmoji.DICE, disable_notification=True)

    # dp.include_router(router)
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

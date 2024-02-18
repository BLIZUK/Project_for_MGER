import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage


import config

from routers import router as main_router


async def main():
    #  Токен берем из другого файла
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

    # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
    # Но явное лучше неявного =]
    dp = Dispatcher(storage=MemoryStorage())

    # Вообще можно имя не указывать и ничего не передавать, но будем соблюдать этику
    router = Router(name=__name__)

    dp.include_router(main_router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

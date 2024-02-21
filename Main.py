#  Подключение библиотек
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

#  Подключение файлов
import config
from routers import router as main_router


async def main():
    #  Токен берем из другого файла
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
    # Но явное лучше неявного =]
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(main_router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


#  Точка входа
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

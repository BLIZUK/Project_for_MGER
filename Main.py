#  Подключение библиотек
import asyncio
import logging
import config

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

#  Подключение хендлеров
from routers import router as main_router


#  Инициализация бота
async def main():
    #  Токен берем из другого файла
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
    # Но явное лучше неявного =]
    dp = Dispatcher(storage=MemoryStorage()) #Как я понимаю Dispatcher хранит в себе состояния бота (FSM). Нужно поменять
    dp.include_router(main_router) # Роутер бота. Штука для декомпозиции. Класс роутер содержит в себе класс диспатчер
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()) #Получение ботом аплейтов


#  Точка входа
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

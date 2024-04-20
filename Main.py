#  Подключение общих библиотек
import asyncio
#  Убрать перед выходом в свет
import logging
import config

#  Подключение библиотек айограма
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

#  Подключение хендлеров
from routers import router as main_router


#  Инициализация бота
async def main():
    #  Токен берем из другого файла
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)

    print(">Dispatcher activ")
    # Если не указать storage, то по умолчанию всё равно будет MemoryStorage
    # Но явное лучше неявного =]
    # Как я понимаю Dispatcher хранит в себе состояния бота (FSM). Нужно поменять (?)
    dp = Dispatcher(storage=MemoryStorage())

    # Роутер бота. Штука для декомпозиции. Класс роутер содержит в себе класс диспатчер
    dp.include_router(main_router)
    print(">Bot activ")
    # Получение ботом аплейтов
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


#  Точка входа
if __name__ == "__main__":
    #  Конструкция нужная для избавления от ошибки, вследствие прекращения работы программы
    try:
        print(">Start program")
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print(">Exit")

# Импорты напрямую из Aiogram
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from routers.handlers.text import help_txt
# Импорт классов состояний
from FSMmachine import Admini, Event

# Взятый роутер из директории admin_handlers a их файла admin_router.py

# Кнопки
from routers.handlers.admin_handlers.admin_button import button_for_event, button_choosing
from routers.handlers.button_defolt import help_buttons_DEF

from routers.handlers.text import ADMINs

# Импортированный класс с методами для базы данных
from database.db import BotDB

router = Router(name=__name__)


@router.message(Admini.chossing, F.text == "Мероприятия")
async def events(message: Message, state: FSMContext):
    await state.set_state(Event.event_choose)
    await message.answer("Выберете дальнейшнее действие.", reply_markup=button_for_event())


@router.message(Event.event_choose, F.text)
async def choosing_event(message: Message, state: FSMContext):
    if message.text == "Создать мероприятие":
        await state.set_state(Event.create_event)
        #await message.answer()
    elif message.text == "Прошедшие мероприятия":
        result = BotDB().get_event(past=True)
        for i in range(len(result)):
            about_event = (f"Название мероприятия: {result[i][0]}\n"
                           f"Дата проведения: {result[i][1]}\n"
                           f"Место: {result[i][2]}")
            await message.answer(about_event)
        #await state.set_state(Event.see_events_complete)
    elif message.text == "Предстоящие мероприятия":
        result = BotDB().get_event(active=True)
        for i in range(len(result)):
            about_event = (f"Название мероприятия: {result[i][0]}\n"
                           f"Дата проведения: {result[i][1]}\n"
                           f"Место: {result[i][2]}")
            await message.answer(about_event)
    elif message.text == "Вернуться назад":
        await state.set_state(Admini.chossing)
        await message.answer(help_txt, reply_markup=button_choosing())
    else:
        await message.answer("Нет такого действия")


@router.message(Event.create_event)
async def create_event_function(message: Message, state: FSMContext):
    pass
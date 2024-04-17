# Импорты напрямую из Aiogram
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command
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


@router.message(Command("off"))
async def off(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    if message.from_user.id == ADMINs:
        await message.answer("Все действия отменены.", reply_markup=button_choosing())
        await state.set_state(Admini.chossing)
    else:
        await message.answer("Все действия отменены.", reply_markup=help_buttons_DEF())


@router.message(Admini.chossing, F.text == "Мероприятия")
async def events(message: Message, state: FSMContext):
    if message.from_user.id == ADMINs:
        await state.set_state(Event.event_choose)
        await message.answer("Выберете дальнейшнее действие.", reply_markup=button_for_event())


@router.message(Event.event_choose, F.text)
async def choosing_event(message: Message, state: FSMContext):
    if message.text == "Создать мероприятие":
        pass
        #await state.set_state(Event.create_event)
    elif message.text == "Прошедшие мероприятия":
        pass
        #await state.set_state(Event.see_events_complete)
    elif message.text == "Предстоящие мероприятия":
        result = BotDB().get_event()
        for i in range(len(result)):
            about_event = (f"Название мероприятия: {result[i][0]}\n"
                           f"Дата проведения: {result[i][1]}\n"
                           f"Место: {result[i][2]}")
            await message.answer(about_event)
    else:
        await message.answer("Нет такого действия")


@router.message(Event.create_event, F.text)
async def create_event_function(message: Message, state: FSMContext):
    pass

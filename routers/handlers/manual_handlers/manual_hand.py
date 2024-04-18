from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from FSMmachine import Manualuser
from database.db import BotDB


router = Router(name=__name__)


@router.message(Manualuser.choosing, F.text == "Мероприятия")
async def cmd_test1(message: Message, state: FSMContext):
    # Андрей, форматирование на тебе
    result = BotDB().get_event(active=True)
    for i in range(len(result)):
        about_event = (f"Название мероприятия: {result[i][0]}\n"
                       f"Дата проведения: {result[i][1]}\n"
                       f"Место: {result[i][2]}")
        await message.answer(about_event)


@router.message(Manualuser.choosing, F.text == "Предложить идею" or "предложить идею")
async def cmd_test2(message: Message, state: FSMContext):
    # Андрей, форматирование на тебе
    await message.answer("Какое-то отформатированное сообщение типа")


@router.message(Manualuser.send_to_adm, F.text)
async def send_message_to_adm(message: Message, state: FSMContext):
    pass

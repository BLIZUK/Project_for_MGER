#  Подключение библиотек
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from ..database.admin_button import button_send
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from FSMmachine import Manualuser
#  Импортируем кнопки из файла button_defolt.py
from .button_defolt import help_buttons_DEF
#  Импортируем текст из файла text.py
from .text import (welcome, help_txt, help_end_txt, ID_all_peopl,
                   ADMIN, ADMINs, welcome_for_manuall,
                   help_txt_manuall)
from ..database.db import BotDB

router = Router(name=__name__)


class Sign(StatesGroup):
    add_name = State()


# Включение чата и вызов приветственного ответа
@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if (not BotDB().user_exists(user_id)):
        BotDB().add_user(user_id)
    if message.from_user.id == ADMINs:
        # await message.answer(f"<b>{message.from_user.full_name}</b>," + welcome + f"\nТвой ID: {message.from_user.id}"
        # f"", parse_mode=ParseMode.HTML)
        await message.answer(welcome)
    else:
        await message.answer(welcome_for_manuall + "\n/help - для получения дальнейшей информации")

    if (BotDB().name_exists(user_id)):
        await message.answer("Введите своё ФИО по образцу 'Иванов Иван Иванович'")
        await state.set_state(Sign.add_name)


#  Вызывает окно с командами
@router.message(Command("help"))
async def cmd_help(message: Message):
    if message.from_user.id == ADMINs:
        await message.answer(help_txt, reply_markup=button_send())
    else:
        await message.answer(help_txt_manuall, reply_markup=help_buttons_DEF())


#  Из базы даннных достатся информация о предстоящих мероприятих
@router.message(F.text.lower() == "Мероприятия" or "мероприятия")
async def cmd_test1(message: Message, state: FSMContext):
    # Андрей, форматирование на тебе 
    await message.answer("Какое-то отформатированное сообщение типа")
    await state.set_state(Manualuser.event_see)


#  Пишет сообщение админу, предложение какой-то идеи
@router.message(F.text.lower() == "Предложить идею" or "предложить идею")
async def cmd_test2(message: Message, state: FSMContext):
    # Андрей, форматирование на тебе 
    await message.answer("Какое-то отформатированное сообщение типа")
    await state.set_state(Manualuser.send_to_adm)


@router.message(Sign.add_name, F.text)
async def add_fullname_default(message: Message, state: FSMContext):
    mailing = message.text
    BotDB().add_fullname(mailing, message.from_user.id)
    await state.clear()


@router.message(Manualuser.event_see)
async def active_events_user(message: Message, state: FSMContext):
    events = BotDB().get_event
    print(events)
    await message.answer("") 

@router.message(Manualuser.send_to_adm, F.text)
async def send_message_to_adm(message: Message, state: FSMContext):
    pass
#  Отправление ID юзера
# @router.message(F.text.lower() == "мой id")
# async def cmd_test_id(message: Message):
# await message.reply(f"Твой ID: {message.from_user.id}")


#  Проверка на отправку сообщения по ID чата с выбором человека
# @router.message(Command("test3"))
# async def cmd_test3(message: Message, bot: Bot):
# await message.reply("Делаю", reply_markup=ReplyKeyboardRemove())

# @router.message(F.text.lower() == "андрей")
# async def send_emoji_id(message: Message):
# await bot.send_dice(ID_peopl["андрей"], emoji=DiceEmoji.DICE)

# @router.message(F.text.lower() == "ваня")
# async def send_emoji_id(message: Message):
# await bot.send_dice(ID_peopl["ваня"], emoji=DiceEmoji.SLOT_MACHINE)

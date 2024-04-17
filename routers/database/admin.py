#  Подключение библиотек
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums.parse_mode import ParseMode
from aiogram.methods.delete_message import DeleteMessage
from .admin_button import buttons_admin_off, button_choose_send, button_send, button_for_event
from FSMmachine import Conditionstep, Event, Admini, Sign
from .db import BotDB

#  Отдельно выделю машину состояний, а точнее FSM, как объект
from aiogram.fsm.context import FSMContext

#  Импортируем кнопки из файла button_defolt.py


#  Импортируем текст из файла text.py и прочие вещи
from ..handlers.text import ADMIN, ID_all_peopl, ID_glad_people, ADMINs

router = Router(name=__name__)


#   ЭТИ 4 ОБРАБОТЧИКА ОТВЕЧАЮТ ЗА РАССЫЛКУ СООБЩЕНИЙ АКТИВИСТАМ ОТ АДМИНА. РАБОТАЮТ В РЕЖИМЕ ЗАПИСИ
@router.message(Admini.chossing, F.text == "Рассылка")
async def pick_method(message: Message, state: FSMContext):
    if message.from_user.id == ADMINs:
        await state.set_state(Conditionstep.choosing_sender_of_message)
        await message.answer("Выберите режим рассылки: ", reply_markup=button_choose_send())


@router.message(Conditionstep.choosing_sender_of_message, F.text.lower())
async def choose(message: Message, state: FSMContext):
    if message.text == "Рассылка для доверенных лиц":
        await state.set_state(Conditionstep.choosing_sender_of_message_not_all)
        await message.reply('Выбран режим рассылки для доверенных лиц. '
                            'Пересылка работает в режиме записи. Для её завершения напишите "Off".',
                            reply_markup=buttons_admin_off())

    elif message.text == "Общая рассылка":
        await state.set_state(Conditionstep.choosing_sender_of_message_all)
        await message.reply('Выбран режим рассылки для всех активистов. '
                            'Пересылка работает в режиме записи. Для её завершения напишите "Off".',
                            reply_markup=buttons_admin_off())
    elif message.text == "Off":
        await state.clear()
        await message.answer("Рассылка отменена.", reply_markup=button_send())
        return
    else:
        await message.reply("Вы выбрали некорректный режим рассылки.")


@router.message(Conditionstep.choosing_sender_of_message_not_all, F.text)
async def write_send_not_all(message: Message, bot: Bot, state: FSMContext):
    mail = message.text
    if message.text == "Off":
        await state.clear()
        await message.answer("Рассылка заверщена.", reply_markup=button_send())
        return
    for key in ID_glad_people:
        await bot.send_message(ID_glad_people[key], mail + f"\nby <b>{message.from_user.full_name}</b>",
                               disable_notification=True, parse_mode=ParseMode.HTML)


@router.message(Conditionstep.choosing_sender_of_message_all, F.text)
async def write_send_all(message: Message, bot: Bot, state: FSMContext):
    mail = message.text
    if message.text == "Off":
        await state.clear()
        await message.answer("Рассылка заверщена.", reply_markup=button_send())
        return
    for key in ID_all_peopl:
        await bot.send_message(ID_all_peopl[key], mail + f"\nby <b>{message.from_user.full_name}</b>",
                               disable_notification=True, parse_mode=ParseMode.HTML)


@router.message(Admini.chossing, F.text == "Мероприятия")
async def events(message: Message, state: FSMContext):
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


# Вышла пустышка, самая настоящая. В будущем она переместиться в панель инструментолв и оттуда уже будет нести пользу
@router.message(Command("off"))
async def off(message: Message, state: FSMContext):
    await message.answer("Все действия отменены.")
    await state.clear()


# @router.message(Command("edit"))
# async def editor(message: Message, state: FSMContext):
#     await state.set_state(Stepofedit.edit_defolt)
#     await message.answer("Введите имя активиста по образцу 'Иванов Иван Иванович'.")


# @router.message(Stepofedit.edit_defolt, F.text)
# async def edit_name(message: Message, state: FSMContext):
#     mailing = message.text
#     mailing.split(" ")

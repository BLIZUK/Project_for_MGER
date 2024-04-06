#  Подключение библиотек
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.methods.delete_message import DeleteMessage
from .admin_button import buttons_admin_off, button_choose, button_send

#  Отдельно выделю машину состояний, а точнее FSM, как объект
from aiogram.fsm.context import FSMContext

#  Импортируем кнопки из файла button_defolt.py


#  Импортируем текст из файла text.py и прочие вещи
from ..handlers.text import ADMIN, ID_all_peopl, ID_glad_people, ADMINs

router = Router(name=__name__)


class Conditionstep(StatesGroup):
    #  Состояния бота в виде класса и его атрибутов для рассылки
    choosing_sender_of_message = State()
    choosing_sender_of_message_not_all = State()
    choosing_sender_of_message_all = State()


class Stepofedit(StatesGroup):
    #  Состояния для редактировния активиста в базе данных
    edit_defolt = State()
    edit_name = State()
    edit_surname = State()
    edit_father_name = State()
    edit_bithday = State()
    edit_pervichka = State()
    edit_photo = State()
    edit_phone = State()


#   ЭТИ 3 ОБРАБОТЧИКА ОТВЕЧАЮТ ЗА РАССЫЛКУ СООБЩЕНИЙ АКТИВИСТАМ ОТ АДМИНА. РАБОТАЮТ В РЕЖИМЕ ЗАПИСИ
@router.message(F.text == "Рассылка")
async def pick_method(message: Message, state: FSMContext):
    if message.from_user.id == ADMINs:
        await state.set_state(Conditionstep.choosing_sender_of_message)
        await message.answer("Выберите режим рассылки: ", reply_markup=button_choose())


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

    else:
        await state.clear()
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


@router.message(Command("edit"))
async def editor(message: Message, state:  FSMContext):
    await state.set_state(Stepofedit.edit_defolt)
    await message.answer("Введите имя активиста по образцу 'Иванов Иван Иванович'.")

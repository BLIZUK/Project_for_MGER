# Импорты напрямую из Aiogram
from aiogram import F, Bot, Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

# Импорт классов состояний
from FSMmachine import Admini, Conditionstep

# Взятый роутер из директории admin_handlers a их файла admin_router.py
from database.db import BotDB

# Кнопки
from routers.handlers.admin_handlers.admin_button import button_choose_send, buttons_admin_off, button_choosing

# Текст и прочее
from routers.handlers.text import ID_all_peopl

router = Router(name=__name__)


#   ЭТИ 4 ОБРАБОТЧИКА ОТВЕЧАЮТ ЗА РАССЫЛКУ СООБЩЕНИЙ АКТИВИСТАМ ОТ АДМИНА. РАБОТАЮТ В РЕЖИМЕ ЗАПИСИ
@router.message(Admini.chossing, F.text == "Рассылка")
async def pick_method(message: Message, state: FSMContext):
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
        await state.set_state(Admini.chossing)
        await message.answer("Рассылка отменена.", reply_markup=button_choosing())
        return
    else:
        await message.reply("Вы выбрали некорректный режим рассылки.")


@router.message(Conditionstep.choosing_sender_of_message_not_all, F.text)
async def write_send_not_all(message: Message, bot: Bot, state: FSMContext):
    mail = message.text
    result = BotDB().get_users(status_in_base=2)
    if message.text == "Off":
        await state.set_state(Admini.chossing)
        await message.answer("Рассылка заверщена.", reply_markup=button_choosing())
        return
    for key in result:
        await bot.send_message(key[0], mail + f"\nby <b>{message.from_user.full_name}</b>",
                               disable_notification=True, parse_mode=ParseMode.HTML)


@router.message(Conditionstep.choosing_sender_of_message_all, F.text)
async def write_send_all(message: Message, bot: Bot, state: FSMContext):
    mail = message.text
    if message.text == "Off":
        await state.set_state(Admini.chossing)
        await message.answer("Рассылка заверщена.", reply_markup=button_choosing())
        return
    for key in ID_all_peopl:
        await bot.send_message(ID_all_peopl[key], mail + f"\nby <b>{message.from_user.full_name}</b>",
                               disable_notification=True, parse_mode=ParseMode.HTML)

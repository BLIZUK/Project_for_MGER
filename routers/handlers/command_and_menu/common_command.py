from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from FSMmachine import Sign, Admini, Manualuser
from database.db import BotDB
from routers.handlers.button_defolt import help_buttons_DEF
from routers.handlers.text import ADMINs, welcome, welcome_for_manuall, help_txt, help_txt_manuall
from routers.handlers.admin_handlers.admin_button import  button_choosing

router = Router(name=__name__)


@router.message(Command("off"))
async def off(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    if message.from_user.id == ADMINs:
        await message.answer("Все действия отменены.", reply_markup=button_choosing())
    else:
        await message.answer("Все действия отменены.", reply_markup=help_buttons_DEF())


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if not BotDB().user_exists(user_id):
        BotDB().add_user(user_id)
    if BotDB().name_exists(user_id):
        await message.answer("Введите своё ФИО по образцу 'Иванов Иван Иванович'")
        await state.set_state(Sign.add_name)
    else:
        if message.from_user.id == ADMINs:
            # await message.answer(f"<b>{message.from_user.full_name}</b>," + welcome + f"\nТвой ID: {message.from_user.id}"
            # f"", parse_mode=ParseMode.HTML)
            await message.answer(welcome)

        else:
            await message.answer(welcome_for_manuall + "\n/help - для получения дальнейшей информации")


@router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    if message.from_user.id == ADMINs:
        await state.set_state(Admini.chossing)
        await message.answer(help_txt, reply_markup=button_choosing())
    else:
        await state.set_state(Manualuser.choosing)
        await message.answer(help_txt_manuall, reply_markup=help_buttons_DEF())


@router.message(Sign.add_name, F.text)
async def add_fullname_default(message: Message, state: FSMContext):
    mailing = message.text
    BotDB().add_fullname(mailing, message.from_user.id)
    await cmd_start(message, state)

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from FSMmachine import Sign, Admini, Manualuser
from database.db import BotDB
from routers.handlers.button_defolt import help_buttons_def, check_id_inline_button
from routers.handlers.text import welcome, welcome_for_manuall, help_txt, help_txt_manuall
from routers.handlers.admin_handlers.admin_button import button_choosing

router = Router(name=__name__)


@router.message(Command("off"))
async def off(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    id_ = await pick_status(message.from_user.id)
    if message.from_user.id == id_:
        await message.answer("Все действия отменены.", reply_markup=button_choosing())
    else:
        await message.answer("Все действия отменены.", reply_markup=help_buttons_def())


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if not BotDB().user_exists(user_id):
        BotDB().add_user(user_id)
    if BotDB().name_exists(user_id):
        await message.answer("Введите своё ФИО по образцу 'Иванов Иван Иванович'")
        await state.set_state(Sign.add_name)
    else:
        id_ = await pick_status(message.from_user.id)
        if message.from_user.id == id_:
            # await message.answer(f"<b>{message.from_user.full_name}</b>," + welcome + f"\nТвой ID: {
            # message.from_user.id}" f"", parse_mode=ParseMode.HTML))
            await message.answer(welcome)

        else:
            await message.answer(welcome_for_manuall + "\n/help - для получения дальнейшей информации",
                                 reply_markup=check_id_inline_button())


@router.message(Command("help"))
async def cmd_help(message: Message, state: FSMContext):
    id_ = await pick_status(message.from_user.id)
    if message.from_user.id == id_:
        await state.set_state(Admini.chossing)
        await message.answer(help_txt, reply_markup=button_choosing())
    else:
        await state.set_state(Manualuser.choosing)
        await message.answer(help_txt_manuall, reply_markup=help_buttons_def())


@router.message(Sign.add_name, F.text)
async def add_fullname_default(message: Message, state: FSMContext):
    mailing = message.text
    BotDB().add_fullname(mailing, message.from_user.id)
    await cmd_start(message, state)


@router.callback_query(F.data == "Посмотреть мой id")
async def check_id(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(f"Ваш id - {callback.message.from_user.id}")


async def pick_status(id_):
    result = BotDB().get_users(status_in_base=1)
    for row in result:
        if id_ in row:
            return id_
    return None

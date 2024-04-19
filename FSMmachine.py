# Импорты всего необходимого для FSM машины
from aiogram.fsm.state import State, StatesGroup


class Sign(StatesGroup):
    add_name = State()
    close_sign_up = State()


class Event(StatesGroup):
    event_choose = State()
    create_event = State()
    see_events_complete = State()
    see_events_active = State()


class Activist(StatesGroup):
    pass


class Admini(StatesGroup):
    chossing = State()


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


class Manualuser(StatesGroup):
    # Состояние для обычных юзеров
    choosing = State()
    event_see = State()
    send_to_adm = State()

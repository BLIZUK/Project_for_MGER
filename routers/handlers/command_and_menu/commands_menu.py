from aiogram import Bot, Router
from aiogram.types import BotCommand

router = Router(name=__name__)


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command="/start",
                   description="Начало работы с ботом"),
        BotCommand(command='/help',
                   description='Справка по работе бота'),
        BotCommand(command='/off',
                   description='Сброс состояний бота'),
        BotCommand(command='/support',
                   description='Поддержка')
    ]
    await bot.set_my_commands(main_menu_commands)

router.startup.register(set_main_menu)
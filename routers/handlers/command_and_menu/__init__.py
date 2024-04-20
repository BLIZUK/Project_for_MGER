# Файл переносчик
__all__ = ("router",)

from aiogram import Router
from routers.handlers.command_and_menu.commands_menu import router as menu__router
from routers.handlers.command_and_menu.common_command import router as command__router

router = Router(name=__name__)

router.include_routers(menu__router, command__router)

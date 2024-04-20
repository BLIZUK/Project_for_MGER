#  Файл переносчик
__all__ = ("router", )

from aiogram import Router

from .command_and_menu import router as command_router
from .manual_handlers import router as manual_router
from .admin_handlers import router as admin_router

router = Router()

router.include_routers(command_router, manual_router, admin_router)
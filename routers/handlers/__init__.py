#  Файл переносчик
__all__ = ("router", )

from aiogram import Router

from .admin_handlers import router as admin_router
from .command_and_menu import router as command_router
from .manual_handlers import router as manual_router

router = Router()


router.include_routers(admin_router, command_router, manual_router)

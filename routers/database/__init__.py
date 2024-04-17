#  Файл переносчик
__all__ = ("router",)

from aiogram import Router
from .db import router as database_router
from .admin import router as admin_router

router = Router()

router.include_routers(admin_router, database_router)

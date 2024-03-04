#  Файл переносчик
__all__ = ("router",)

from aiogram import Router
from .db import router as database_router

router = Router()

router.include_router(database_router)

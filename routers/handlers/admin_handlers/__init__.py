# Файл переносчик
__all__ = ("router",)

from aiogram import Router
from .events import router as events_router
from .send_to_users import router as send_router

router = Router(name=__name__)

router.include_routers(events_router, send_router)

__all__ = ("router",)

from aiogram import Router
from .manual_hand import router as manual__router

router = Router(name=__name__)

router.include_routers(manual__router)

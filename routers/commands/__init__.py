__all__ = ("router", )

from aiogram import Router

from .essential_commands import router as essential_commands_router
from .user_commands import router as user_commands_router

router = Router()

router.include_routers(
    essential_commands_router,
    user_commands_router
)

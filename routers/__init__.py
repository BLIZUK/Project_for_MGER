<<<<<<< HEAD
__all__ = ("router", )

from aiogram import Router

from .commands import router as commands_router

router = Router(name=__name__)

router.include_router(commands_router)
=======
#  Файл переносчик
__all__ = ("router",)

from aiogram import Router
from .handlers import router as handlers_router
from .database import router as data_router

router = Router(name=__name__)

router.include_routers(handlers_router, data_router)
>>>>>>> origin/Vanya

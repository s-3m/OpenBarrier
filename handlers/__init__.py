from aiogram import Router

from .commands import router as command_router
from .call_back import router as call_back_router

router = Router()
router.include_routers(command_router, call_back_router)
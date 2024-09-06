from aiogram import Router

from.command_handlers import router as handle_router

router = Router()
router.include_router(handle_router)
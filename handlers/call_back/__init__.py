from aiogram import Router

from .call_back_routers import router as cb_router

router = Router()
router.include_router(cb_router)
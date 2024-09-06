import asyncio
import json
import os
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import router as handler_routers
from db import db_dict


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(handler_routers)


async def main():
    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)


if __name__ == '__main__':

    asyncio.run(main())

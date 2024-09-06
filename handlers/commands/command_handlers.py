import asyncio
import json
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from  aiogram import Router
from db import db_dict

from keyboards import get_open_inline_keyboard


router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f'Привет {message.from_user.full_name}!'
                         f'\nТеперь ты можешь пользоваться шлагбаумом!')
    user_id = str(message.from_user.id)
    user = db_dict.get(user_id)

    if not user:
        db_dict[user_id] = {}
        db_dict[user_id]['name'] = message.from_user.full_name
        db_dict[user_id]['status'] = False
        with open('db_file.json', 'a+') as file:
            json.dump(db_dict, file)


@router.message(Command('open'))
async def to_open_handler(message: Message):
    await message.answer('Выберете шлагбаум:',reply_markup=get_open_inline_keyboard())
    await asyncio.sleep(10)
    await message.delete()

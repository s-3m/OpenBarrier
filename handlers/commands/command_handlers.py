import asyncio
import json
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from  aiogram import Router

from db import db_dict
from utils.json_wrighter import json_wright
from keyboards import get_open_inline_keyboard, allow_access_inline_keyboard


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
        db_dict[user_id]['enter'] = False
        db_dict[user_id]['status'] = "user"
        db_dict[user_id]['access'] = "off"

        json_wright()


@router.message(Command('open'))
async def to_open_handler(message: Message):
    user_id = str(message.from_user.id)
    if db_dict[user_id]['access'] == "on" or db_dict[user_id]['status'] == "admin":
        await message.answer('Выберете шлагбаум:',reply_markup=get_open_inline_keyboard())
        await asyncio.sleep(10)
        await message.delete()
    else:
        await message.answer('У вас нет доступа. Запросите доступ, выбрав команду /access в меню.')



@router.message(Command('access'))
async def to_request_access(message: Message):
    user_id = str(message.from_user.id)
    await message.answer('Запрос доступа отправлен. Вам придёт уведомление о результате.')
    await message.bot.send_message('259811443',
                                   f'{user_id} запрашивает доступ.\n Разрешаем?',
                                   reply_markup=allow_access_inline_keyboard(user_id))
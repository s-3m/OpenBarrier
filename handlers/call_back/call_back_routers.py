import asyncio

from aiogram import Router, F
from aiogram.client.session import aiohttp
from aiogram.types import CallbackQuery

from db import db_dict
from utils.help_params_mobile import headers, data

router = Router()


@router.callback_query(F.data.startswith('barrier'))
async def open_barrier_cb(call_back: CallbackQuery):
    barrier_number = call_back.data.split('_')[1]
    user = str(call_back.from_user.id)
    async with aiohttp.ClientSession() as session:
        async with session.post('https://lk.amvideo-msk.ru/api/api4.php', headers=headers, data=data[barrier_number]) as response:
            result: dict = await response.json(content_type='text/html')
            result: str = result['str']
            status_code = response.status
    if status_code == 200:
        user_enter = db_dict.get(user)['name'] if db_dict.get(user) else 'Неизвестный дикобраз'
        await call_back.answer(f'Шлагбаум {barrier_number} открывается!', cache_time=5)
        user_status = 'заехал' if db_dict.get(user)['status'] == False else 'выехал'
        await call_back.bot.send_message(259811443, f'{user_enter} {user_status} через шлагбаум {barrier_number}')
        db_dict[user]['status'] = not db_dict[user]['status']
        print(db_dict)
    else:
        await call_back.answer(f'Упс! Что-то пошло не так.')

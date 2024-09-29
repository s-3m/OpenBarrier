import asyncio

from aiogram import Router, F
from aiogram.client.session import aiohttp
from aiogram.types import CallbackQuery

from db import db_dict
from utils.help_params_mobile import headers, data
from keyboards import CbAccessData, get_wait_temporary_kb, get_open_inline_keyboard
from utils.json_wrighter import json_wright

router = Router()


@router.callback_query(F.data.startswith('barrier'))
async def open_barrier_cb(call_back: CallbackQuery):
    barrier_number = call_back.data.split('_')[1]
    user = str(call_back.from_user.id)
    if db_dict[user]["access"] == "on":
        await call_back.message.edit_reply_markup(reply_markup=get_wait_temporary_kb())
        async with aiohttp.ClientSession() as session:
            async with session.post('https://lk.amvideo-msk.ru/api/api4.php', headers=headers,
                                    data=data[barrier_number]) as response:
                result: dict = await response.json(content_type='text/html')
                result: str = result['str']
                status_code = response.status
        if status_code == 200:
            user_enter = db_dict.get(user)['name'] if db_dict.get(user) else 'Неизвестный дикобраз'
            await call_back.answer(f'🚗 Шлагбаум {barrier_number} открывается!', cache_time=5)
            user_status = '🟢 заехал' if db_dict.get(user)['enter'] is False else '🔴 выехал'
            if user != '259811443':
                await call_back.bot.send_message(259811443,
                                                 f'{user_enter} {user_status} через шлагбаум {barrier_number}')
                db_dict[user]['enter'] = not db_dict[user]['enter']
                json_wright()
        else:
            await call_back.answer(f'Упс! Что-то пошло не так.')
        await asyncio.sleep(5)
        await call_back.message.edit_reply_markup(reply_markup=get_open_inline_keyboard())
    else:
        await call_back.bot.send_message(user, '⛔ Доступ был ограничен. Вы можете запросить доступ снова.')


@router.callback_query(CbAccessData.filter())
async def allow_access_cb(callback_query: CallbackQuery, callback_data: CbAccessData):
    user_id = callback_data.user_id
    if callback_data.access:
        db_dict[user_id]["access"] = "on"
        json_wright()
        await callback_query.answer("🟢 Доступ был разрешён!")
        await callback_query.bot.send_message(user_id, "Вам был разрешён доступ к управлению шлагбаумом!")
    else:
        await callback_query.answer("⛔ Доступ был запрещён!")
        await callback_query.bot.send_message(user_id, "Доступ к управлению шлагбаумом был запрещён!")

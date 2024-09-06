from sys import prefix

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_open_inline_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text='1', callback_data='barrier_1'),
        InlineKeyboardButton(text='2', callback_data='barrier_2'),
    )
    builder.row(
        InlineKeyboardButton(text='3', callback_data='barrier_3'),
        InlineKeyboardButton(text='4', callback_data='barrier_4'),
    )
    return builder.as_markup()



class CbAccessData(CallbackData, prefix="acess_data"):
    user_id: str
    access: bool


def allow_access_inline_keyboard(user_id, ) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    cb_data_yes = CbAccessData(user_id=user_id, access=True)
    cb_data_no = CbAccessData(user_id=user_id, access=False)
    builder.row(
        InlineKeyboardButton(text='Да', callback_data=cb_data_yes.pack()),
    )
    builder.row(
        InlineKeyboardButton(text='Нет', callback_data=cb_data_no.pack()),
    )
    builder.adjust(1)

    return builder.as_markup()
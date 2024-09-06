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
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def addresses_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='пункт выдачи павер №1', callback_data='addresses_1'),
        InlineKeyboardButton(text='пункт выдачи 2', callback_data='addresses_2'),
        width=2
    )
    return builder.as_markup()

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
urlkb = InlineKeyboardMarkup(row_width=1)
b1 = InlineKeyboardButton(text='wildberries', url='https://www.wildberries.ru')

urlkb.add(b1)
colkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='help', callback_data='www'))


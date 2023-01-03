from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from parser_films_kinogo_life2 import *

user_kb = InlineKeyboardMarkup(resize_keybord=True).add(
    InlineKeyboardButton('Получить фильм', callback_data='films_buttons')
)

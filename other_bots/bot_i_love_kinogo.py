from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from parser_films_kinogo_life2 import *
from buttons import *
import random


bot = Bot('5958293925:AAGh2IVIUkvGfygLO-ebFbIzU-r0QfZJnAA')
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я бот который подскажет какой фильм можно посмотреть🍿🎬', reply_markup=user_kb)


@dp.callback_query_handler(text='films_buttons')
async def films_buttons(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    mess = random.choice(spend)
    await bot.send_message(callback_query.from_user.id, f'{mess}', reply_markup=user_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

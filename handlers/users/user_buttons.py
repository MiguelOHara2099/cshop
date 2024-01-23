# imports
from aiogram import types
from loader import dp
from keyboards import catalog_list
from loader import bot

@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Покупать товар у него: @qwertyopka')

@dp.message_handler(text='Корзина')
async def cart(message: types.Message):
    await message.answer(f'Корзина пуста!')

@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст!', reply_markup=catalog_list)
    
#callback_data in client_cb.py
@dp.callback_query_handler()
async def callback_query_keyboard(callback_query: types.CallbackQuery):
    if callback_query.data == 'geely':
        await bot.set_message(chat_id=callback_query.from_user.id, text='вы выбрали geely')
    elif callback_query.data == 'chery':
        await bot.set_message(chat_id=callback_query.from_user.id, text='вы выбрали geely')
    elif callback_query.data == 'changan':
        await bot.set_message(chat_id=callback_query.from_user.id, text='вы выбрали geely')
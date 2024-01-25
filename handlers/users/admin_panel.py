# imports
from aiogram import types
from loader import dp
from keyboards import admin_panel
from data.config import admins_id

@dp.message_handler(text='Admin-панель')
async def admin(message: types.Message):
    if message.from_user.id in admins_id:
        await message.answer(f'Вы вошли в админ-панель', reply_markup=admin_panel)
    else:
        await message.reply('Я тебя не понимаю.')
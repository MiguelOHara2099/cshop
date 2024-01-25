# imports
from aiogram import types
from loader import dp
from keyboards import main_admin, main
from data.config import admins_id

# FSM start on command /offer
@dp.message_handler(text="/start")
async def command_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMJZa1i1sUceYCrcDk1WCPp-H7Ph-cAAu0UAAKD-xFKXtAkmdrg8cY0BA')
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в магазин автомобильных запчастей!', reply_markup=main)
    if message.from_user.id in admins_id:
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=main_admin)
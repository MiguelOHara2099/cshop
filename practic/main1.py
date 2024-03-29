from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer_sticker('CAACAgIAAxkBAAMJZa1i1sUceYCrcDk1WCPp-H7Ph-cAAu0UAAKD-xFKXtAkmdrg8cY0BA')
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в магазин автомобильных запчастей!', reply_markup=main)
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы авторизовались как администратор!', reply_markup=main_admin)

# @dp.message_handler(commands=['id'])
# async def cmd_id(message: types.Message):
#     await message.answer(f'{message.from_user.id}')

@dp.message_handler(text='Admin-панель')
async def admin(message: types.Message):
    if message.from_user.id == int(os.getenv('ADMIN_ID')):
        await message.answer(f'Вы вошли в админ-панель', reply_markup=admin_panel)
    else:
        await message.reply('Я тебя не понимаю.')

@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
    await message.answer(f'Покупать товар у него: @qwertyopka')

@dp.message_handler(text='Корзина')
async def cart(message: types.Message):
    await message.answer(f'Корзина пуста!')

@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer(f'Каталог пуст!', reply_markup=catalog_list)

# @dp.message_handler(content_types=['sticker'])
# async def check_sticker(message: types.Message):
#     await message.answer(message.sticker.file_id)
#     # получение гроуп айди через стикер
#     await bot.send_message(message.from_user.id, message.chat.id)

# @dp.message_handler(content_types=['document', 'photo'])
# async def forward_message(message: types.Message):
#     await bot.forward_message(os.getenv('GROUP_ID'), message.from_user.id, message.message_id)

@dp.message_handler()
async def answer(message: types.Message):
    await message.reply('Я тебя не понимаю.')
    
if __name__ == '__main__':
    executor.start_polling(dp)
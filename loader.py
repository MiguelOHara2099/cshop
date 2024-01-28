from aiogram import Bot, Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

# storage = MemoryStorage()

bot = Bot(token=config.BOT_TOKEN) #, parse_mode=enums.parse_mode.ParseMode.HTML)
dp = Dispatcher(bot=bot) 
async def on_startup(dp):
	from utils.notify_admins import on_startup_notify
	await on_startup_notify(dp)
	
	from utils.set_bot_commands import set_default_commands
	await set_default_commands(dp)
	
	print("bot started")

if __name__ == "__main__":
	from aiogram import dispatcher
	from handlers import dp
	
	dispatcher.start_polling(dp, on_startup=on_startup)

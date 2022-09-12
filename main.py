from tkinter import Misc
from aiogram.utils import executor
from components import dp
from handlers import admin, misc, user 
from database import sqlite_db

async def on_startup(_):
    print("Connection to the server is successful")
    sqlite_db.sql_startup()

user.register_handlers_user(dp)
admin.register_handlers_admin(dp)
misc.register_handlers_misc(dp)

executor.start_polling(dp,skip_updates=True,on_startup=on_startup)
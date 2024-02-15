# - *- coding: utf- 8 - *-
import asyncio
import os
import sys
import logging

import colorama
from aiogram import Dispatcher, Bot

from bot.data.config import bot_token, database

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s', level=logging.INFO)
colorama.init()

loop = asyncio.get_event_loop()
loop.create_task(database.create_database())

# Запуск бота
async def main():
    dp = Dispatcher()  
    bot = Bot(token=bot_token, parse_mode="HTML")
    try:
        print(colorama.Fore.LIGHTBLUE_EX + f"BOT WAS STARTED!")
        print(colorama.Fore.RESET)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        

if __name__ == "__main__":
    loop.run_until_complete(main())
    loop.close()
    
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("BOT WAS STOPPED!")
    finally:
        if sys.platform.startswith("win"):
            os.system("cls")
        else:
            os.system("clear")

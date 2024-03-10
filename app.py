import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from database.engine import create_db, drop_db, session_maker

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from keyboards.main_menu import set_main_menu
from middlewares.db import DataBaseSession

ALLOWED_UPDATES = ['message, edited_message']

logger = logging.getLogger(__name__)

bot = Bot(token=os.getenv('TOKEN'), parse_mode="HTML")
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def on_startup(bot):

    run_param = False
    if run_param:
        await drop_db()
    await create_db()

async def on_shutdown(bot):
    print('Бот лег!')


async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '               
                               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    await bot.send_message(id=ID_MAIN_ADMIN, text='Бот запущен!')
    await set_main_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
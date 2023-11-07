from os import getenv
import logging

from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv

from bot import handlers


async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(*handlers.routers)
    load_dotenv()
    bot = Bot(getenv('BOT_TOKEN'), parse_mode='HTML')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

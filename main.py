import asyncio
import logging
import sys

from aiogram.enums import ParseMode

from env import BOT_TOKEN, BOT_REMINDER_DAY_TIME
from handlers.day_handler import day_router
from handlers.graph_handler import graph_router

from aiogram import Bot, Dispatcher

from reminder import reminder


async def main() -> None:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(day_router)
    dp.include_router(graph_router)

    asyncio.ensure_future(reminder.start(bot, BOT_REMINDER_DAY_TIME))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

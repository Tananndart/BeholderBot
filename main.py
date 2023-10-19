import asyncio
import logging

from aiogram.enums import ParseMode

from env import BOT_TOKEN, BOT_REMINDER_TIME, LOG_LEVEL
from handlers.day_handler import day_router
from handlers.graph_handler import graph_router

from aiogram import Bot, Dispatcher

from reminder import reminder


async def main() -> None:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(day_router)
    dp.include_router(graph_router)

    logging.info(f"Start reminder by {BOT_REMINDER_TIME}")
    asyncio.ensure_future(reminder.start(BOT_TOKEN, BOT_REMINDER_TIME))

    logging.info(f"Start bot pooling")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=LOG_LEVEL, format='%(asctime)s %(levelname)s: %(message)s')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from env import BOT_TOKEN
from handlers.day_handler import day_router
from handlers.graph_handler import graph_router


async def main() -> None:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_router(day_router)
    dp.include_router(graph_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

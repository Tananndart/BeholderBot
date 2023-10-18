import asyncio
import logging
from datetime import datetime

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from env import BOT_CHAT_ID, BOT_TOKEN
from repository.repository_factory import get_day_repository


async def send_remind(bot: Bot):
    day_status_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="👍", callback_data="good_day_callback"),
                          InlineKeyboardButton(text="👌", callback_data="norm_day_callback"),
                          InlineKeyboardButton(text="👎", callback_data="bad_day_callback")]])

    logging.info(f"Reminder send question about day status")
    await bot.send_message(BOT_CHAT_ID, f"Как прошел день?", reply_markup=day_status_keyboard)


async def send_current_day_status(bot: Bot, status: int):
    status_from_user = "непонятно..."
    if status == 1:
        status_from_user = "отлично!"
    elif status == 0:
        status_from_user = "нормально!"
    elif status == -1:
        status_from_user = "плохо!"

    logging.info(f"Reminder send message about current day status {status}")
    await bot.send_message(BOT_CHAT_ID, f"Твой день прошел {status_from_user}")


async def check(bot: Bot, remind_time: str, max_delay_sec: int):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == remind_time:
            logging.info(f"Reminder check {current_time}")

            current_date = datetime.now().date()
            current_status = get_day_repository().get_status_day(current_date)

            if current_status:
                await send_current_day_status(bot, current_status)
            else:
                await send_remind(bot)

        await asyncio.sleep(max_delay_sec)


async def start(bot_token: str, remind_time: str, max_delay_sec: int = 60):
    bot = Bot(bot_token, parse_mode=ParseMode.HTML)

    current_sec = int(datetime.now().strftime("%S"))
    delay = max_delay_sec - current_sec
    if delay == max_delay_sec:
        delay = 0

    await asyncio.sleep(delay)
    await check(bot, remind_time, max_delay_sec)

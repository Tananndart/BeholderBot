import asyncio
from datetime import datetime

from aiogram import Bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from env import BOT_CHAT_ID
from repository.repository_factory import get_day_repository


async def send_remind(bot: Bot):
    day_status_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="👍", callback_data="good_day_callback"),
                          InlineKeyboardButton(text="👌", callback_data="norm_day_callback"),
                          InlineKeyboardButton(text="👎", callback_data="bad_day_callback")]])

    await bot.send_message(BOT_CHAT_ID, f"Как прошел день?", reply_markup=day_status_keyboard)


async def check(bot: Bot, remind_time: str, max_delay_sec: int):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == remind_time:
            current_date = datetime.now().date()
            if not get_day_repository().exist_day(current_date):
                await send_remind(bot)
        await asyncio.sleep(max_delay_sec)


async def start(bot: Bot, remind_time: str, max_delay_sec: int = 60):
    current_sec = int(datetime.now().strftime("%S"))
    delay = max_delay_sec - current_sec
    if delay == max_delay_sec:
        delay = 0

    await asyncio.sleep(delay)
    await check(bot, remind_time, max_delay_sec)

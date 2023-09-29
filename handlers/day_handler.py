from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message

from repository.repository_factory import get_day_repository

day_router = Router()


async def _day_handler(message: Message, day_status: int) -> None:
    day_date = message.date.date()

    day_repository = get_day_repository()
    day_repository.save_day(day_date, day_status)

    await message.reply(text=f"Date = {day_date}; Status = {day_status}")


@day_router.message(Command("day_good"))
async def handle_day(message: Message):
    await _day_handler(message, 1)


@day_router.message(Command("day_norm"))
async def handle_day(message: Message):
    await _day_handler(message, 0)


@day_router.message(Command("day_bad"))
async def handle_day(message: Message):
    await _day_handler(message, -1)

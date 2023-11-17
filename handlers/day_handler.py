import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from domain.day import DayStatus, Day
from repository.repository_factory import get_day_repository

day_router = Router()


async def _day_handler(message: Message, day_status: DayStatus) -> None:
    new_day = Day(message.date.date(), day_status)

    day_repository = get_day_repository()
    day_repository.save_day(new_day)

    logging.info(f"Save day: date = {new_day.date}, status == {new_day.status}")
    await message.reply(text=f"Date = {new_day.date}; Status = {new_day.status}")


@day_router.message(Command("day_good"))
async def handle_day(message: Message):
    logging.info("Call command day_good")
    await _day_handler(message, DayStatus.GOOD)


@day_router.message(Command("day_norm"))
async def handle_day(message: Message):
    logging.info("Call command day_norm")
    await _day_handler(message, DayStatus.NORMAL)


@day_router.message(Command("day_bad"))
async def handle_day(message: Message):
    logging.info("Call command day_bad")
    await _day_handler(message, DayStatus.BAD)


@day_router.callback_query(F.data.in_(['good_day_callback']))
async def process_buttons_press(callback: CallbackQuery):
    logging.info("Call good_day_callback")
    await _day_handler(callback.message, DayStatus.GOOD)


@day_router.callback_query(F.data.in_(['norm_day_callback']))
async def process_buttons_press(callback: CallbackQuery):
    logging.info("Call norm_day_callback")
    await _day_handler(callback.message, DayStatus.NORMAL)


@day_router.callback_query(F.data.in_(['bad_day_callback']))
async def process_buttons_press(callback: CallbackQuery):
    logging.info("Call bad_day_callback")
    await _day_handler(callback.message, DayStatus.BAD)

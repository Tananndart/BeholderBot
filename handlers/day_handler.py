from pydoc import html

from aiogram import Bot, Router
from aiogram.filters import Command, ExceptionTypeFilter
from aiogram.types import ErrorEvent, Message

from repository.repository_factory import get_day_repository
from tools.tools import get_text_without_command

day_router = Router()


class InvalidDayStatus(Exception):
    pass


@day_router.message(Command("day"))
async def handle_day(message: Message):
    day_status = get_text_without_command(message.text)
    if not day_status:
        raise InvalidDayStatus(f"Day status can't be None!")

    day_statuses = {"good": 1, "norm": 0, "bad": -1}
    day_status = str(day_status).lower()
    if day_status not in day_statuses.keys():
        raise InvalidDayStatus(f"Day status {day_status} not in {day_statuses.keys()}")

    day_repository = get_day_repository()
    day_date = message.date.date()
    day_status = day_statuses[day_status]
    day_repository.save_day(day_date, day_status)

    await message.reply(text=f"Your Day status = {day_status}")


@day_router.errors(ExceptionTypeFilter(InvalidDayStatus))
async def handle_invalid_day_exception(event: ErrorEvent, bot: Bot) -> None:
    assert isinstance(event.exception, InvalidDayStatus)
    # logger.error("Error caught: %r while processing %r", event.exception, event.update)

    assert event.update.message is not None
    chat_id = event.update.message.chat.id

    text = html.escape(repr(event.exception))
    await bot.send_message(chat_id=chat_id, text=text)

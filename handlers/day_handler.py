from pydoc import html

from aiogram import Bot, Router
from aiogram.filters import Command, ExceptionTypeFilter
from aiogram.types import ErrorEvent, Message

from tools.tools import get_message_text

day_router = Router()
DAY_STATUSES = ["good", "norm", "bad"]


class InvalidDayStatus(Exception):
    pass


@day_router.message(Command("day"))
async def handle_day(message: Message):
    day_status = get_message_text(message)
    if not day_status:
        raise InvalidDayStatus(f"Day status can't be None!")

    day_status = str(day_status).lower()
    if day_status not in DAY_STATUSES:
        raise InvalidDayStatus(f"Day status {day_status} not in {DAY_STATUSES}")

    await message.reply(text=f"Your Day status = {day_status}")


@day_router.errors(ExceptionTypeFilter(InvalidDayStatus))
async def handle_invalid_day_exception(event: ErrorEvent, bot: Bot) -> None:
    assert isinstance(event.exception, InvalidDayStatus)
    # logger.error("Error caught: %r while processing %r", event.exception, event.update)

    assert event.update.message is not None
    chat_id = event.update.message.chat.id

    text = html.escape(repr(event.exception))
    await bot.send_message(chat_id=chat_id, text=text)

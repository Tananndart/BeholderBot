from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import BufferedInputFile

from repository.repository_factory import get_day_repository
from visualisations.day_visual import DayVisual

graph_router = Router()


@graph_router.message(Command("graph"))
async def handle_graph(message: Message) -> None:
    days_repository = get_day_repository()
    all_data = days_repository.get_all()
    dates = all_data[0]
    statuses = all_data[1]

    image_bytes = DayVisual.visualise(dates, statuses)

    image_input_file = BufferedInputFile(image_bytes, "graph.png")
    await message.reply_photo(photo=image_input_file)

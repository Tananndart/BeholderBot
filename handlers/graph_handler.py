import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import BufferedInputFile

from repository.repository_factory import get_day_repository
from visualisations.day_visual import DayVisual

graph_router = Router()


@graph_router.message(Command("graph"))
async def handle_graph(message: Message) -> None:
    logging.info("Call graph command")

    days_repository = get_day_repository()
    all_days = days_repository.get_all()

    if not all_days:
        logging.info("Graph command not found data from create graph")
        await message.reply("Нет данных для построения графика")
        return

    image_bytes = DayVisual.visualise(all_days)
    image_input_file = BufferedInputFile(image_bytes, "graph.png")

    logging.info("Graph command create and send graph")
    await message.reply_photo(photo=image_input_file)

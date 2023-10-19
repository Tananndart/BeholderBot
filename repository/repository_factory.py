from env import BOT_DATA_PATH
from repository.csv_day_repository import CsvDayRepository
from repository.day_repository import DayRepository


def get_day_repository() -> DayRepository:
    return CsvDayRepository(BOT_DATA_PATH + r"/day_data.csv")

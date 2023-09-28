from abc import ABC, abstractmethod
from datetime import date


class DayRepository(ABC):
    @abstractmethod
    def save_day(self, day_date: date, day_status: int) -> None:
        pass

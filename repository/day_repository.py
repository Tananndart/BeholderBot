from abc import ABC, abstractmethod
from datetime import date
from typing import List, Any


class DayRepository(ABC):
    @abstractmethod
    def save_day(self, day_date: date, day_status: int) -> None:
        pass

    @abstractmethod
    def get_all(self, with_headers: bool = False) -> List[List[Any]]:
        pass

from abc import ABC, abstractmethod
from datetime import date
from typing import List, Any, Union

from domain.day import Day, DayStatus


class DayRepository(ABC):
    @abstractmethod
    def save_day(self, day: Day) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Day]:
        pass

    @abstractmethod
    def get_status_day(self, day_date: date) -> Union[DayStatus, None]:
        pass

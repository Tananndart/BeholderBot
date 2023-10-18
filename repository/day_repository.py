from abc import ABC, abstractmethod
from datetime import date
from typing import List, Any, Union


class DayRepository(ABC):
    @abstractmethod
    def save_day(self, day_date: date, day_status: int) -> None:
        pass

    @abstractmethod
    def get_all(self, with_headers: bool = False) -> List[List[Any]]:
        pass

    @abstractmethod
    def get_status_day(self, day_date: date) -> Union[int, None]:
        pass

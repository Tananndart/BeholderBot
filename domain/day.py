from datetime import date
from enum import Enum


class DayStatus(Enum):
    BAD = -1
    NORMAL = 0
    GOOD = 1

    def __str__(self):
        if self.value == -1:
            return "Плохо"
        elif self.value == 0:
            return "Нормально"
        elif self.value == 1:
            return "Хорошо"


class Day:
    def __init__(self, day_date: date = None, day_status: DayStatus = None):
        self.date = day_date
        self.status = day_status

    def __eq__(self, other):
        if isinstance(other, Day):
            return self.date == other.date and self.status == other.status
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

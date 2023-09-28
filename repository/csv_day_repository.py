import csv
import os
from datetime import date, datetime
from typing import List, Any

from repository.day_repository import DayRepository


class CsvDayRepository(DayRepository):

    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Status"])

    def save_day(self, day_date: date, day_status: int) -> None:
        with open(self.csv_file_path, mode="a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([day_date, day_status])

    def get_all(self, with_headers: bool = False) -> List[List[Any]]:
        dates = []
        statuses = []

        with open(self.csv_file_path, "r", newline='') as file:
            reader = csv.reader(file)

            if not with_headers:
                next(reader)

            for row in reader:
                day_date = datetime.strptime(row[0], "%Y-%m-%d").date()
                day_status = int(row[1])

                dates.append(day_date)
                statuses.append(day_status)

        return [dates, statuses]

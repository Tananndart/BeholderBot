import csv
import os
from datetime import date
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
            #f.write(f"{day_date},{day_status}\n")

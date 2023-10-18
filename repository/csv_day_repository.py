import csv
import os
from datetime import date, datetime
from typing import List, Any, Union
import pandas as pd

from repository.day_repository import DayRepository


class CsvDayRepository(DayRepository):

    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Status"])

    def save_day(self, day_date: date, day_status: int) -> None:
        df = pd.read_csv(self.csv_file_path)

        day_date_str = str(day_date)
        if day_date_str in df['Date'].values:
            index = df[df['Date'] == day_date_str].index[0]
            df.loc[index, 'Status'] = day_status
        else:
            df.loc[len(df.index)] = [day_date_str, day_status]

        df.to_csv(self.csv_file_path, index=False)

    def get_all(self, with_headers: bool = False) -> List[List[Any]]:
        dates = []
        statuses = []

        with open(self.csv_file_path, "r", newline='') as file:
            reader = csv.reader(file)

            if not with_headers:
                next(reader)

            for row in reader:
                day_date = self._str_to_date(row[0])
                day_status = int(row[1])

                dates.append(day_date)
                statuses.append(day_status)

        return [dates, statuses]

    def get_status_day(self, day_date: date) -> Union[int, None]:
        with open(self.csv_file_path, "r", newline='') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                current_day_date = self._str_to_date(row[0])
                if current_day_date == day_date:
                    day_status = int(row[1])
                    return day_status

        return None

    @staticmethod
    def _str_to_date(date_str: str):
        return datetime.strptime(date_str, "%Y-%m-%d").date()

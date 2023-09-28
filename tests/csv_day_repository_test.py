import csv
import os
import pytest
from datetime import date, datetime
from repository.csv_day_repository import CsvDayRepository


def test_first_init() -> None:
    """
    Проверить первичную инициализацию репозитория.
    Должен быть создан новый csv файл в двумя колонками: Date,Status.
    """
    # Arrange
    csv_path = r"days_data_test.csv"
    first_col_str = "Date"
    second_col_str = "Status"

    # Act
    CsvDayRepository(csv_path)

    # Assert
    assert (os.path.isfile(csv_path))
    with open(csv_path, mode="r", newline='') as f:
        reader = csv.reader(f)
        headers = reader.__next__()
        assert (first_col_str == headers[0])
        assert (second_col_str == headers[1])

    # Clean
    os.remove(csv_path)


def test_save_day() -> None:
    """
    Сохраняет один день в csv и проверяет корректность сохраненных данных.
    """
    # Arrange
    csv_path = r"days_data_test.csv"
    day_repository = CsvDayRepository(csv_path)

    day_date_str = "2023-08-10"
    day_date = datetime.strptime(day_date_str, "%Y-%m-%d").date()
    day_status = 1

    # Act
    day_repository.save_day(day_date, day_status)

    # Assert
    with open(csv_path, mode="r", newline='') as f:
        reader = csv.reader(f)
        headers = reader.__next__()
        first_row = reader.__next__()
        assert (day_date_str == first_row[0])
        assert (day_status == int(first_row[1]))

    # Clean
    os.remove(csv_path)

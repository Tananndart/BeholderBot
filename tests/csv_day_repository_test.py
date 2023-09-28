import csv
import os
import pytest
from datetime import datetime
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


def test_get_all():
    """
    Записывает несколько строк, затем получает все данные и сверяет с записанным.
    """
    # Arrange
    csv_path = r"days_data_test.csv"
    test_dates_str = ["2023-08-10", "2023-09-10", "2023-10-10", "2023-11-10"]
    test_dates = []
    for date_str in test_dates_str:
        test_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        test_dates.append(test_date)

    test_statuses = [1, 0, -1, 1]

    day_repository = CsvDayRepository(csv_path)

    for i in range(len(test_dates)):
        day_date = test_dates[i]
        day_status = int(test_statuses[i])
        day_repository.save_day(day_date, day_status)

    # Act
    all_data = day_repository.get_all()

    # Assert
    assert (test_dates == all_data[0])
    assert (test_statuses == all_data[1])

    # Clean
    os.remove(csv_path)

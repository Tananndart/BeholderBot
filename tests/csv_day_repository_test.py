import csv
import os
import pytest
from datetime import datetime, date

from domain.day import DayStatus, Day
from repository.csv_day_repository import CsvDayRepository

TEST_CSV_PATH = r"days_data_test.csv"


@pytest.fixture(autouse=True)
def before_tests():
    if os.path.exists(TEST_CSV_PATH):
        os.remove(TEST_CSV_PATH)


def _to_date(text: str) -> date:
    return datetime.strptime(text, "%Y-%m-%d").date()


def test_first_init() -> None:
    """
    Проверить первичную инициализацию репозитория.
    Должен быть создан новый csv файл в двумя колонками: Date,Status.
    """
    # Arrange
    first_col_str = "Date"
    second_col_str = "Status"

    # Act
    CsvDayRepository(TEST_CSV_PATH)

    # Assert
    assert (os.path.isfile(TEST_CSV_PATH))
    with open(TEST_CSV_PATH, mode="r", newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        assert (first_col_str == headers[0])
        assert (second_col_str == headers[1])


def test_save_day() -> None:
    """
    Сохраняет один день в csv и проверяет корректность сохраненных данных.
    """
    # Arrange
    day_repository = CsvDayRepository(TEST_CSV_PATH)

    day_date_str = "2023-08-10"
    day_raw_status = 1
    day = Day(_to_date(day_date_str), DayStatus(day_raw_status))

    # Act
    day_repository.save_day(day)

    # Assert
    with open(TEST_CSV_PATH, mode="r", newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        first_row = next(reader)
        assert (day_date_str == first_row[0])
        assert (day_raw_status == int(first_row[1]))


def test_save_day_if_day_already_exist() -> None:
    """
    Сохраняет уже существующий день в csv.
    Должен найти перезаписать запись с уже сохраненным днем.
    """
    # Arrange
    day_repository = CsvDayRepository(TEST_CSV_PATH)

    already_save_day = ("2023-08-10", 0)
    new_save_day = ("2023-08-10", 1)

    test_days = [("2023-08-09", 0), already_save_day, ("2023-08-11", 0)]
    for day in test_days:
        new_day = Day(_to_date(day[0]), DayStatus(day[1]))
        day_repository.save_day(new_day)

    # Act

    day_repository.save_day(Day(_to_date(new_save_day[0]), DayStatus(new_save_day[1])))

    # Assert
    already_save_day_find = False
    with open(TEST_CSV_PATH, mode="r", newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            if new_save_day[0] == row[0]:
                already_save_day_find = True
                assert (new_save_day[1] == int(row[1]))

    assert already_save_day_find


def test_get_all():
    """
    Записывает несколько дней, затем получает все дни и сверяет с записанными.
    """
    # Arrange
    test_days_data = [("2023-08-10", 1), ("2023-09-10", 0), ("2023-10-10", -1), ("2023-11-10", 1)]
    test_days = [Day(_to_date(d[0]), DayStatus(d[1])) for d in test_days_data]

    day_repository = CsvDayRepository(TEST_CSV_PATH)
    for day in test_days:
        day_repository.save_day(day)

    # Act
    all_data = day_repository.get_all()

    # Assert
    assert test_days == all_data


def test_get_status_day():
    """
    Получает статус существующего дня, и получает статус несуществующего дня (None).
    """
    # Arrange
    test_days_data = [("2023-08-10", 1), ("2023-09-11", 0), ("2023-10-01", -1)]
    test_days = [Day(_to_date(d[0]), DayStatus(d[1])) for d in test_days_data]

    exist_day = test_days[1]

    day_repository = CsvDayRepository(TEST_CSV_PATH)
    for day in test_days:
        day_repository.save_day(day)

    # Act
    status_exist_day = day_repository.get_status_day(exist_day.date)
    status_not_exist_day = day_repository.get_status_day(_to_date("2024-09-11"))

    # Assert
    assert status_exist_day == exist_day.status
    assert status_not_exist_day is None

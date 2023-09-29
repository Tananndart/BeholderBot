import csv
import os
import pytest
from datetime import datetime
from repository.csv_day_repository import CsvDayRepository


TEST_CSV_PATH = r"days_data_test.csv"


@pytest.fixture(autouse=True)
def before_tests():
    if os.path.exists(TEST_CSV_PATH):
        os.remove(TEST_CSV_PATH)


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
        headers = reader.__next__()
        assert (first_col_str == headers[0])
        assert (second_col_str == headers[1])


def test_save_day() -> None:
    """
    Сохраняет один день в csv и проверяет корректность сохраненных данных.
    """
    # Arrange
    day_repository = CsvDayRepository(TEST_CSV_PATH)

    day_date_str = "2023-08-10"
    day_date = datetime.strptime(day_date_str, "%Y-%m-%d").date()
    day_status = 1

    # Act
    day_repository.save_day(day_date, day_status)

    # Assert
    with open(TEST_CSV_PATH, mode="r", newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        first_row = next(reader)
        assert (day_date_str == first_row[0])
        assert (day_status == int(first_row[1]))


def test_get_all():
    """
    Записывает несколько строк, затем получает все данные и сверяет с записанным.
    """
    # Arrange
    test_dates_str = ["2023-08-10", "2023-09-10", "2023-10-10", "2023-11-10"]
    test_dates = []
    for date_str in test_dates_str:
        test_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        test_dates.append(test_date)

    test_statuses = [1, 0, -1, 1]

    day_repository = CsvDayRepository(TEST_CSV_PATH)

    for i in range(len(test_dates)):
        day_date = test_dates[i]
        day_status = int(test_statuses[i])
        day_repository.save_day(day_date, day_status)

    # Act
    all_data = day_repository.get_all()

    # Assert
    assert (test_dates == all_data[0])
    assert (test_statuses == all_data[1])

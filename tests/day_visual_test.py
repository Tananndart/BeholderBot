import io
import os

from PIL import Image
import pytest

from repository.csv_day_repository import CsvDayRepository
from visualisations.day_visual import DayVisual


TEST_CSV_PATH = r"days_data_test.csv"


@pytest.fixture(autouse=True)
def before_tests():
    if os.path.exists(TEST_CSV_PATH):
        os.remove(TEST_CSV_PATH)

    _generate_csv_with_days()


def test_visual_day():
    """
    Получает визуализацию за все дни и проверяет корректность картинки.
    Саму картинку не анализирует.
    """
    # Arrange
    day_repository = CsvDayRepository(TEST_CSV_PATH)
    all_days = day_repository.get_all()

    # Act
    image_data = DayVisual.visualise(all_days)

    # Assert
    try:
        image_stream = io.BytesIO(image_data)
        image = Image.open(image_stream)
        image.verify()
    except (IOError, SyntaxError) as e:
        pytest.fail(f"Test_visual_day exception: {e}")


def _generate_csv_with_days():
    import csv
    import random
    from datetime import datetime, timedelta

    start_date = datetime(2023, 8, 1)
    end_date = datetime(2023, 8, 31)
    date_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

    statuses = [1, 0, -1]
    status_data = [random.choice(statuses) for _ in range(len(date_range))]
    status_data[0] = 0

    data = [["Date", "Status"]]
    for i in range(len(date_range)):
        data.append([date_range[i].strftime("%Y-%m-%d"), status_data[i]])

    with open(TEST_CSV_PATH, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

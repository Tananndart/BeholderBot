import io
import os

from PIL import Image
import pytest

from repository.csv_day_repository import CsvDayRepository
from visualisations.day_visual import DayVisual


def test_visual_day():
    """
    Получает визуализацию за все дни и проверяет корректность картинки.
    Саму картинку не анализирует.
    """
    # Arrange
    csv_path = r"days_data_test.csv"
    day_repository = CsvDayRepository(csv_path)
    all_data = day_repository.get_all()
    dates = all_data[0]
    statuses = all_data[1]

    # Act
    image_data = DayVisual.visualise(dates, statuses)

    # Assert
    try:
        image_stream = io.BytesIO(image_data)
        image = Image.open(image_stream)
        image.verify()
    except (IOError, SyntaxError) as e:
        pytest.fail(f"Test_visual_day exception: {e}")

    # Clean
    os.remove(csv_path)


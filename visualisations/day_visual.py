import io
from datetime import date
from typing import List

import matplotlib.pyplot as plt

from domain.day import Day


class DayVisual:
    @staticmethod
    def visualise(days: List[Day]) -> bytes:
        dates = [day.date for day in days]
        statuses = [day.status.value for day in days]

        calculated_statuses = [sum(statuses[:i + 1]) for i in range(len(statuses))]
        formatted_dates = [d.strftime("%d-%m-%Y") for d in dates]

        plt.set_loglevel('WARNING')
        plt.plot(formatted_dates, calculated_statuses)
        plt.title("Status over Time")

        for i in range(len(formatted_dates)):
            plt.scatter(formatted_dates[i], calculated_statuses[i], color='black', marker='o')

        plt.xticks(rotation=90)
        plt.tight_layout()

        image_stream = io.BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)
        image_bytes = image_stream.read()
        image_stream.close()
        plt.close()

        return image_bytes

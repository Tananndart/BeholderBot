import io
from datetime import date
from typing import List

import matplotlib.pyplot as plt


class DayVisual:
    @staticmethod
    def visualise(dates: List[date], statuses: List[int]) -> bytes:
        calculated_statuses = []
        value = 0
        for status in statuses:
            value += status
            calculated_statuses.append(value)

        plt.plot(dates, calculated_statuses)
        plt.xlabel("Date")
        plt.ylabel("Status")
        plt.title("Status over Time")

        for i in range(len(dates)):
            plt.scatter(dates[i], calculated_statuses[i], color='black', marker='o')

        plt.xticks(rotation=90)
        plt.tight_layout()

        image_stream = io.BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)
        image_bytes = image_stream.read()
        image_stream.close()
        plt.close()

        return image_bytes

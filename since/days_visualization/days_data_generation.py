"""
Generate random csv days data format:
Date,Status
2023-08-01,Good
2023-08-02,Good
2023-08-03,Norm
...
2023-08-31,Bad
"""

if __name__ == "__main__":
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

    with open("days_data.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSV create successful!")

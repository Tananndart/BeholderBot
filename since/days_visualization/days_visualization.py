"""
Get days_data.csv and create visualization
"""
import csv
import matplotlib.pyplot as plt

if __name__ == "__main__":
    dates = []
    statuses = []

    # read csv
    with open("days_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        value = 0
        for row in reader:
            dates.append(row[0])
            current_state = int(row[1])
            value += current_state
            statuses.append(value)

    # build graph
    plt.plot(dates, statuses)
    plt.xlabel("Date")
    plt.ylabel("Status")
    plt.title("Status over Time")

    # set dots
    for i in range(len(dates)):
        plt.scatter(dates[i], statuses[i], color='black', marker='o')

    plt.xticks(rotation=90)
    plt.show()

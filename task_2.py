import csv
with open("task_2.csv", "w+", newline='') as output_file:
    output = csv.writer(output_file)
    output.writerow(["sale", "date", "region"])

    # read through data_0
    with open("data/daily_sales_data_0.csv", "r") as file_0:
        csvFile = csv.reader(file_0)
        next(csvFile)
        for entry in csvFile:
            if entry[0] != "pink morsel":
                continue
            sale = float(entry[1][1:]) * float(entry[2])
            output.writerow([sale, entry[3], entry[4]])

    # read through data_1
    with open("data/daily_sales_data_1.csv", "r") as file_1:
        csvFile = csv.reader(file_1)
        next(csvFile)
        for entry in csvFile:
            if entry[0] != "pink morsel":
                continue
            sale = float(entry[1][1:]) * float(entry[2])
            output.writerow([sale, entry[3], entry[4]])

    # read through data_2
    with open("data/daily_sales_data_2.csv", "r") as file_2:
        csvFile = csv.reader(file_2)
        next(csvFile)
        for entry in csvFile:
            if entry[0] != "pink morsel":
                continue
            sale = float(entry[1][1:]) * float(entry[2])
            output.writerow([sale, entry[3], entry[4]])

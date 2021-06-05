import csv

def read_csv(filename):
    data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(str(row[0]).lower().strip())
    return data

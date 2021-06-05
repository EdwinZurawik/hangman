import csv


def read_csv(filename):
    data = []
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(str(row[0]).lower().strip())
    except FileNotFoundError:
        data = []
        print(f"Couldn't locate the file: {filename}. "
              "Please check the filename and path.")
    return data

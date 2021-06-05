import os
import csv
from src import helpers


def test_read_csv_not_existing_file():
    filepath = os.path.join(os.path.dirname(os.getcwd()), "not_extisting.csv")

    assert helpers.read_csv(filepath) == []


def test_read_csv_correct_file():
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "test.csv")
    data = ["first", "second", "third"]

    create_file(filepath, data)

    assert helpers.read_csv(filepath) == data
    os.remove(filepath)


def test_read_csv_empty_file():
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "test.csv")
    data = []

    create_file(filepath, data)

    assert helpers.read_csv(filepath) == data
    os.remove(filepath)


def create_file(filepath, data):

    with open(filepath, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for item in data:
            row = [item]
            csv_writer.writerow(row)


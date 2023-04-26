import csv
import os
from os_path.os_path_scripts import resources
csv_path = os.path.join(resources, 'eggs.csv')


# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_csv_file():
    with open(csv_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile)
        name_list = []
        for row in csvreader:
            name_list.append(row)
    assert name_list[0] == ['Anna', 'Pavel', 'Peter']
    assert name_list[2] == ['Alex', 'Serj', 'Yana']

import csv

file = open('songs.csv', encoding="utf-8")
csvreader = csv.reader(file)


def vaild_length():
    return 2


for row in csvreader:
    if not row:
        continue
    if len(row) < vaild_length():
        raise RuntimeError(f'Length row is not valid \n {row}')

import csv

file = open('default_songs.csv', encoding="utf-8")
csvreader = csv.reader(file)


def vaild_length():
    return 3


for row in csvreader:
    if len(row) != vaild_length():
        raise RuntimeError(f'Length row is not valid \n {row}')

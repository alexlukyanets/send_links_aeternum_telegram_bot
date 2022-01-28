import csv

file = open('default_songs.csv', encoding="utf-8")
csvreader = csv.reader(file)

for row in csvreader:
    print(len(row))

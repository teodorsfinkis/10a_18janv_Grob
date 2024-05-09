import csv

with open('file.csv') as fails:
    reader = csv.reader(fails)
    for row in reader:
        print(row[3])
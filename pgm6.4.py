import csv
with open('C:\'names.csv', 'r',) as file:
    reader = csv.reader(file)
for row in reader:
print(row)

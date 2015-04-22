import string
import csv
import random

labels = string.ascii_uppercase[:20]
print labels

for f in labels:
    one = open("{}1.csv".format(f), 'w')
    two = open("{}2.csv".format(f), 'w')
    csvwrtr1 = csv.writer(one)
    csvwrtr2 = csv.writer(two)
    csvwrtr1.writerow(['ID', 'Var1'])
    csvwrtr2.writerow(['ID', 'Var2'])
    for ID in range(500):
        row = [ID, random.choice(range(20))]
        csvwrtr2.writerow(row)
        if random.random() < .8:
            row = [ID, round(random.random(),3)]
            csvwrtr1.writerow(row)
    one.close()
    two.close()

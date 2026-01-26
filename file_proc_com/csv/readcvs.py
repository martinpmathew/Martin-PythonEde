import os
import csv


with open(os.getcwd() + '\\file_proc_com\\csv\\contacts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # for row in reader:
    #     print(row)

    for row in reader:
        print(', '.join(row))

with open(os.getcwd() + '\\file_proc_com\\csv\\contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], ':', row['Phone'])
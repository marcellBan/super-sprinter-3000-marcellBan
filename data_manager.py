'''
data manager for Super Sprinter 3000
persists data in local csv file
by night5word (Marcell Bán)
'''

import csv
from constants import DATA_FILE, FIELDS


def load_data():
    '''returns a dict of dicts containing the current data in the database'''
    data = dict()
    with open(DATA_FILE) as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=FIELDS, delimiter=';', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            data[row['id']] = row
    return data


def save_data(data):
    '''writes the dicts in the given dict to the datafile'''
    with open(DATA_FILE, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDS, delimiter=';', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            writer.writerow(row)

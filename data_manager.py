'''
data manager for Super Sprinter 3000
persists data in local csv file
by night5word (Marcell Bán)
'''

import csv
import os
from constants import DATA_FILE, FIELDS


def load_data():
    '''returns a dict of dicts containing the current data in the database'''
    data = dict()
    if os.path.isfile(DATA_FILE):
        with open(DATA_FILE) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=FIELDS,
                                    delimiter=';', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                row['id'] = int(row['id'])
                data[row['id']] = row
                data[row['id']]['business_value'] = int(data[row['id']]['business_value'])
    return data


def save_data(data):
    '''saves a dict of dicts to the database'''
    with open(DATA_FILE, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDS, delimiter=';', quotechar='|', quoting=csv.QUOTE_NONNUMERIC)
        for row in data:
            writer.writerow(data[row])

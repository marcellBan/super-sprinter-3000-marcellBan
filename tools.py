'''
extra tools used by the Super Sprinter 3000 app
by night5word (Marcell Bán)
'''

from string import digits
from random import choice


def generate_uniqe_id(database, length=8):
    newuid = ''.join([choice(digits) for _ in range(length)])
    while database.get(int(newuid)) is not None:
        newuid = ''.join([choice(digits) for _ in range(length)])
    return int(newuid)

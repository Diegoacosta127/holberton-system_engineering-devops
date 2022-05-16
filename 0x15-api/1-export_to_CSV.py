#!/usr/bin/python3
"""Script that returns info about TODO list progress of an employee"""


import csv
import requests
from sys import argv


if __name__ == "__main__":
    todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
            .format(int(argv[1]))
    users = 'https://jsonplaceholder.typicode.com/users/{}'\
            .format(int(argv[1]))
    done = 0
    tasks = 0
    ret = requests.get(todos).json()
    user = requests.get(users).json()
    with open('{}.csv'.format(argv[1]), 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for elem in ret:
            status = elem.get('completed')
            title = elem.get('title')
            writer.writerow([argv[1], user.get('username'), status, title])

#!/usr/bin/python3
"""Script that returns info about TODO list progress of an employee"""


import requests
from sys import argv


if __name__ == "__main__":
    todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
            .format(argv[1])
    users = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    done = 0
    tasks = 0
    ret = requests.get(todos).json()
    user = requests.get(users).json()
    for elem in ret:
        if elem.get('completed') is True:
            done += 1
        tasks += 1
    print('Employee {} is done with tasks({}/{}):'
          .format(user.get('name'), done, tasks))
    for elem in ret:
        if elem.get('completed') is True:
            print('\t {}'.format(elem.get('title')))

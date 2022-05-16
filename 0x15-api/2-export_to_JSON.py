#!/usr/bin/python3
"""Script that returns info about TODO list progress of an employee"""


import json
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
    with open('{}.json'.format(argv[1]), 'w') as f:
        my_list = []
        for elem in ret:
            my_list.append({'task': elem.get('title'),
                           'completed': elem.get('completed'),
                           'username': user.get('username')})
        final = {'{}'.format(argv[1]): my_list}
        json.dump(final, f)

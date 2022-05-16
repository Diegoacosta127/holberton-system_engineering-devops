#!/usr/bin/python3
"""Script that returns info about TODO list progress of an employee"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    todos = 'https://jsonplaceholder.typicode.com/todos'
    users = 'https://jsonplaceholder.typicode.com/users/'
    ret = requests.get(todos).json()
    user = requests.get(users).json()
    with open('todo_all_employees.json', 'w') as f:
        final = {}
        for item in user:
            id_user = item.get('id')
            my_list = []
            for elem in ret:
                if elem.get('userId') == id_user:
                    my_list.append({'username': item.get('username'),
                                    'task': elem.get('title'),
                                    'completed': elem.get('completed')})
            final[str(id_user)] = my_list
        json.dump(final, f)

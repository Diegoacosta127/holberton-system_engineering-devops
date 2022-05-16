#!/usr/bin/python3
from sys import argv
import requests
import urllib
if __name__ == "__main__":
    done = 0
    tasks = 0
    ret = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(argv[1])).json()
    for elem in ret:
        if elem.get('completed') is True:
            done += 1
        tasks += 1
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(argv[1])).json()
    print('Employee {} is done with tasks ({}/{})'
          .format(users.get('name'), done, tasks))
    for elem in ret:
        if elem.get('completed') is True:
            print('\t{}'.format(elem.get('title')))

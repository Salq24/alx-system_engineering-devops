#!/usr/bin/python3
"""return info abt employee"""


import requests
import sys


if __name__ == '__main__':
    id_emp = sys.argv[1]
    user_api = "https://jsonplaceholder.typicode.com/users"
    link = user_api + '/' + id_emp

    response = requests.get(link)
    name = response.json().get('name')

    tasks = link + '/todos'
    response = requests.get(tasks)
    to_dos = response.json()
    complete = 0
    completed_tasks = []

    for to_do in to_dos:
        if to_do.get('completed'):
            completed_tasks.append(to_do)
            complete += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, complete, len(to_dos)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

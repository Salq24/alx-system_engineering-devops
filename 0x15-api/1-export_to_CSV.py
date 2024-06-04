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

    with open("{}.csv".format(id_emp), 'w') as file:
        for to_do in to_dos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(id_emp, name, to_do.get('completed'),
                               to_do.get('title')))

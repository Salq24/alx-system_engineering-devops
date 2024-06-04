#!/usr/bin/python3
"""return info abt employee"""


import json
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

    m_dict = {id_emp: []}
    for to_do in to_dos:
        m_dict[id_emp].append({
            "task": to_do.get('title'),
            "completed": to_do.get('completed'),
            "username": name})
    with open("{}.json".format(id_emp), 'w') as filenm:
        json.dump(m_dict, filenm)

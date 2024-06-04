#!/usr/bin/python3
"""return info abt employee"""


import sys
import requests
import json


if __name__ == '__main__':
    user_api = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(user_api)
    emps = response.json()

    m_dict = {}
    for emp in emps:
        user_id = emp.get('id')
        username = emp.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        m_dict[user_id] = []
        for task in tasks:
            m_dict[user_id].append({"username": username,
                                    "task": task.get('title'),
                                    "completed": task.get('completed')})
    with open("todo_all_employees.json", 'w') as file:
        json.dump(m_dict, file)

#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employee_id

    response = requests.get(url)
    username = response.json().get('username')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    dictionary = {employee_id: []}
    for task in tasks:
        dictionary[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employee_id), 'w') as filename:
        json.dump(dictionary, filename)

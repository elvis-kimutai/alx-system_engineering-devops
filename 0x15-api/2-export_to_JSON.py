#!/usr/bin/python3
"""
    python script that exports data in the JSON form
"""

from requests import get
from json import dump
from sys import argv

if __name__ == "__main__":
    """
        request user info by employee ID
    """
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    user_name = response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    tasks = response.json()
    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": user_name
                                    })
    with open('{}.json'.format(user_id), 'w') as file:
        dump(dictionary, file)

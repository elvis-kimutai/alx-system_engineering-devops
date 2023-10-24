#!/usr/bin/python3
"""
    python script that exports data in the JSON form
"""
from requests import get
from json import dump

if __name__ == '__main__':
    """
        export to JSON
    """
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    dictionary = {}
    for user1 in users:
        user_id = user1.get('id')
        user_name = user1.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                                        "task": task.get('title'),
                                        "completed": task.get('completed'),
                                        "username": user_name
                                        })
    with open('todo_all_employees.json', 'w') as file:
        dump(dictionary, file)

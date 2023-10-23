#!/usr/bin/python3
"""This module requests the todo list of an employee, and diplay it in
readable format.
EMPLOYEE_NAME and TASK_TITLE
"""

if __name__ == '__main__':
    import requests
    from sys import argv

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))

    to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))

    # deserialize the json data
    # name is a dictionary and numTask is a list of ditionaries
    name = user.json().get('name')
    numTask = len(to_do.json())
    done = 0

    for task in to_do.json():
        if task["completed"] is True:
            done += 1

    print(f'Employee {name} is done with tasks({done}/{numTask}):')
    for task in to_do.json():
        if task["completed"] is True:
            print(f'\t {task["title"]}')

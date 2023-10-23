#!/usr/bin/python3
"""This module requests the todo list of an employee, and diplay it in
json format.
EMPLOYEE_NAME and TASK_TITLE
"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))

    to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))

    my_dict = {}
    emp_task = []
    name = user.json().get('username')

    for task in to_do.json():
        task_dict = {}
        task_dict['task'] = task["title"]
        task_dict['completed'] = task["completed"]
        task_dict['username'] = name
        emp_task.append(task_dict)

    my_dict[argv[1]] = emp_task

    with open(f'{argv[1]}.json', 'w', encoding='utf-8') as json_file:
        # write into the json file
        json.dump(my_dict, json_file)

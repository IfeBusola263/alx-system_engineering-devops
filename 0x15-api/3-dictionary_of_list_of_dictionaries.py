#!/usr/bin/python3
"""This module requests the todo list of all employee, and diplay it in
json format.
"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users')

    to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos')

    my_dict = {}

    # loop through each user
    for user in user.json():

        # make a list of th task of present user
        task_list = []
        for task in to_do.json():

            # compile a dictionary of each task for this user
            task_dict = {}

            # compare id to get specific users to do list
            if user['id'] == task['userId']:
                task_dict['username'] = user['username']
                task_dict['task'] = task['title']
                task_dict['completed'] = task['completed']

            # fill users task list
            if task_dict:
                task_list.append(task_dict)

        # fill master dictionary for all users
        my_dict[user['id']] = task_list

    # saved to json file
    with open('todo_all_employees.json', 'w', encoding='utf-8') as json_file:
        # write into the json file
        json.dump(my_dict, json_file)

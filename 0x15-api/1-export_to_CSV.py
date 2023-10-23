#!/usr/bin/python3
"""This module requests the todo list of an employee, and diplay it in
CSV  format.
EMPLOYEE_NAME and TASK_TITLE
"""

if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))

    to_do = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))

    fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    rows = []
    name = user.json().get('username')

    for task in to_do.json():
        row = []
        row.append(argv[1])
        row.append(name)
        row.append(task["completed"])
        row.append(task["title"])
        rows.append(row)

    with open(f'{argv[1]}.csv', 'w', encoding='utf-8') as csv_file:
        # create a csv writer object
        writer = csv.writer(csv_file)

        # writing the column title or fields
        writer.writerow(fields)

        # write the data
        writer.writerows(rows)

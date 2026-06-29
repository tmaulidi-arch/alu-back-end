#!/usr/bin/python3
"""
Exports employee TODO list data to JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    user_response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    )
    user = user_response.json()
    todos_response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    )
    todos = todos_response.json()
    task_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        }
        task_list.append(task_dict)
    data = {user_id: task_list}
    filename = "{}.json".format(user_id)
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

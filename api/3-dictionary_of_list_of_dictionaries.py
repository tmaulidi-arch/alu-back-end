#!/usr/bin/python3
"""Exports all employees TODO list data to JSON format."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()
    data = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        data[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user.get("id")
        ]
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)

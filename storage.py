import json
import os

# Creating a varaible for the json file
file_name = "tasks.json"

# A function used to load tasks from the json file to python(i.e. parsing)
def load_tasks():
    # Checks if the json file doesnt exist to create it by itself and return an empty list
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump([], file, indent=3)
        return []
    
    # Chesks if the file exist so as to read from the json file and return the information it contains as a list
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)

# A function that takes tasks as an argumentand saves it to the json file 
def save_tasks(tasks):
    with open(file_name, "w") as file:
        json.dump(tasks, file, indent=3)
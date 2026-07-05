from storage import load_tasks as load, save_tasks
from models import create_task
from datetime import datetime

# A function used to add task decription when called in the CLI
def add_task(description):

    # A varable used to load tasks available before adding a new one
    tasks = load()

    # Checks if tasks is empty or not so as to keep adding or just start a new one with a new ID
    if tasks:
        new_id = tasks[-1]["id"] + 1
    else:
        new_id = 1
    
    # A variable used to call the create_task function so as to take in the ID and description to be added as an argument (i.e. new_id)
    new_task = create_task(new_id, description)
    tasks.append(new_task) # Adds the task to the loaded taskss
    save_tasks(tasks) # Saves the task to the json file
    print("Task added successfully!")

# A helper function that prints out each task
def display_task(task):
    print(f"Task ID: {task['id']}")
    print(f"Description: {task['description']}")
    print(f"Status: {task['status']}")
    print(f"Time Created: {task['createdAt']}")
    print(f"Time Updated: {task['updatedAt']}")
    print()

# A functionn used to list all takes in the json file
def list_tasks():
    tasks = load()

    # A condition for looping through each task in tasks in the json file
    for task in tasks:
        display_task(task)

# A function used to delete task from the json file
def delete_task(task_id):
    tasks = load()

    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")

def update_task(task_id, description):
    tasks = load()

    for task in tasks:
        if task['id'] == task_id:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            task['description'] = description
            task['updatedAt'] = current_time
            save_tasks(tasks)
            print("Task updated succesfully!")
            return
        
    print("Task ID Not Found!")

def mark_in_progress(task_id):
    tasks =load()

    for task in tasks:
        if task['id'] == task_id:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            task['status'] = "in-progress"
            task['updatedAt'] = current_time
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    
    print("Task Not Found!")

def mark_done(task_id):
    tasks = load()

    for task in tasks:
        if task['id'] == task_id:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            task['status'] = "done"
            task['upadtedAt'] = current_time
            save_tasks(tasks)
            print("Task completed successfully!")
            return
    
    print("Task Not Found!")
    
def list_tasks_by_status(status):
    tasks  = load()

    for task in tasks:
        if status == task['status']:
            display_task(task)
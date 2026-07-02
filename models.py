from datetime import datetime

# A function that takes in taskID & it's description as an argument and to be called when to create tasks so and to return an object
def create_task(task_id, description):
    
    # A variable used to create time for when tasks are updated an created
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # A dict used to store each task information when called upon to create tasks
    task = {
        "id" : task_id,
        "description" : description,
        "status" : "todo",
        "createdAt" : current_time,
        "updatedAt" : current_time
    }
    return task


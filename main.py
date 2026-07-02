import sys
from task_manager import add_task, list_tasks, delete_task, update_task, mark_in_progress, mark_done

# A variable used to acces the CLI prompt through indexing
command = sys.argv[1]

# A condition to check which operation to be done (i.e. add, delete, list, ....)
if command == "add":
    description = sys.argv[2]
    add_task(description)

elif command == "list":
    list_tasks()

elif command == "delete":
    task_id = int(sys.argv[2])
    delete_task(task_id)

elif command == "update":
    task_id = int(sys.argv[2])
    description = sys.argv[3]
    update_task(task_id, description)

elif command == "mark-in-progress":
    task_id = int(sys.argv[2])
    mark_in_progress(task_id)

elif command == "mark-done":
    task_id= int(sys.argv[2])
    mark_done(task_id)
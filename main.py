import sys
from task_manager import (add_task, list_tasks, delete_task, update_task, mark_in_progress, mark_done, list_tasks_by_status)

# -------------- CHECKS ERR0R HANDLING --------------
if len(sys.argv) < 2:
    print("CLI Usage:")
    print('  python main.py add "Task Description"')
    print("  python main.py update <id> <new description>")
    print("  python main.py delete <id>")
    print("  python main.py mark-in-progress <id>")
    print("  python main.py mark-done <id>")
    print("  python main.py list")
    print("  python main.py list <todo|in-progress|done>")
    sys.exit()

    # A variable used to acces the CLI prompt through indexing
    command = sys.argv[1]

    # -------- ADD -----------
    if command == "add":
        if len(sys.argv) < 3:
            print('Usage: python main.py add "Task Description"')
        else:
            description = sys.argv[2]
            add_task(description)

# ------------- LIST -------------
    elif command == "list":
        
        if len(sys.argv) == 2:
            list_tasks()
        elif len(sys.argv) == 3:
            status = sys.argv[2]
            
            if status not in ['todo', 'in-progress', 'done']:
                print("Invalid status. Choose from: 'done', 'todo', 'in-progress'")
            else:
                list_tasks_by_status(status)
        else:
            print("Usage:")
            print("python main.py list")
            print("python main.py list <todo|in-progress|done>")

# --------------- DELETE ----------------
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python main.py delete <id>")
        else:
            try:
                task_id = int(sys.argv[2])
                delete_task(task_id)
            except ValueError:
                print("Task ID must be a number")

# ----------------- UPDATE --------------------
    elif command == "update":
        if len(sys.argv) < 4:
            print('Usage: python main.py update <id> "New Description"')
        else:
            try:
                task_id = int(sys.argv[2])
                description = sys.argv[3]
                update_task(task_id, description)
            except ValueError:
                print("Task ID must be a number.")

# ------------------ MARK-IN-PROGRESS-------------------
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: python main.py mark-in-progress <id>")
        else:
            try:
                task_id = int(sys.argv[2])
                mark_in_progress(task_id)
            except ValueError:
                print("Task ID must be a number.")
# ----------------- MARK-DONE------------------
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: python main.py mark-done <id>")
        else:
            try:
                task_id = int(sys.argv[2])
                mark_done(task_id)
            except ValueError:
                print("Task ID must be a number.")
else:
    print("Invalid command!")
    print()
    print("CLI commands:")
    print('  add "Task Description"')
    print("  update <id> <new description>")
    print("  delete <id>")
    print("  mark-in-progress <id>")
    print("  mark-done <id>")
    print("  list")
    print("  list <todo|in-progress|done>")
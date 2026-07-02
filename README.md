# 📋 Task Tracker CLI

A simple Command Line Interface (CLI) application built with Python to manage daily tasks. This project allows users to create, update, delete, and organize tasks directly from the terminal while storing data in a JSON file.

## 🚀 Features

- ➕ Add a new task
- ✏️ Update an existing task
- 🗑️ Delete a task
- 📄 List all tasks
- ⏳ Mark a task as **In Progress**
- ✅ Mark a task as **Done**
- 🔍 Filter tasks by status:
  - Todo
  - In Progress
  - Done

## 📂 Project Structure

```
Task-Tracker-CLI/
│
├── main.py             # Entry point of the application
├── task_manager.py     # Task management logic
├── storage.py          # Handles reading/writing JSON data
├── models.py           # Task model
├── tasks.json          # Stores tasks (created automatically)
├── README.md
└── .gitignore
```

## 🛠️ Technologies Used

- Python 3
- JSON
- Python Standard Library
  - `json`
  - `os`
  - `sys`
  - `datetime`

No external libraries or frameworks were used.

## 💻 Usage

### Add a task

```bash
python main.py add "Learn Python"
```

### Update a task

```bash
python main.py update 1 "Master Python"
```

### Delete a task

```bash
python main.py delete 1
```

### Mark a task as In Progress

```bash
python main.py mark-in-progress 1
```

### Mark a task as Done

```bash
python main.py mark-done 1
```

### List all tasks

```bash
python main.py list
```

### List completed tasks

```bash
python main.py list done
```

### List tasks in progress

```bash
python main.py list in-progress
```

### List pending tasks

```bash
python main.py list todo
```

## 📁 Data Storage

Tasks are stored locally in a `tasks.json` file.

Each task contains:

```json
{
    "id": 1,
    "description": "Learn Python",
    "status": "todo",
    "createdAt": "2026-07-03 10:30:00",
    "updatedAt": "2026-07-03 10:30:00"
}
```

## 🎯 What I Learned

This project helped me strengthen my understanding of:

- Working with files in Python
- Reading and writing JSON data
- Command-line arguments (`sys.argv`)
- Functions and modular programming
- Lists and dictionaries
- Error handling
- Project structure and code organization
- Git and GitHub workflow

## 📌 Future Improvements

- Search tasks by keyword
- Add task priorities
- Add due dates
- Sort tasks by date or status
- Colorful terminal output
- Interactive menu mode

## 👨‍💻 Author

**Emmanuel Dairo**

GitHub: https://github.com/emmanueldrivescode

---

This project was built as part of my Python backend development journey to improve my problem-solving skills by building real-world projects.
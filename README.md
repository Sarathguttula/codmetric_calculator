# To-Do List Manager

This project is a console-based To-Do List Manager that allows users to manage their tasks efficiently. It provides functionalities to add, delete, display, and mark tasks as completed. The tasks are stored persistently in a text file.

## Project Structure

```
todo-list-manager
├── src
│   ├── main.py          # Entry point of the application
│   ├── task_manager.py  # Contains the TaskManager class for task management
│   └── utils.py        # Utility functions for string manipulation and file handling
├── tasks.txt           # File to store tasks persistently
└── README.md           # Documentation for the project
```

## Setup Instructions

1. Clone the repository or download the project files.
2. Navigate to the project directory.
3. Ensure you have Python installed on your system.
4. Run the application using the command:

   ```
   python src/main.py
   ```

## Usage

- Upon running the application, you will be presented with a console interface.
- You can use the following commands to manage your tasks:
  - `add <task>`: Adds a new task to the list.
  - `delete <task_id>`: Deletes a task by its ID.
  - `display`: Displays all current tasks.
  - `complete <task_id>`: Marks a task as completed.

## Functionality

The To-Do List Manager allows users to:
- Add new tasks to their to-do list.
- Delete tasks that are no longer needed.
- Display all tasks with their current status.
- Mark tasks as completed, which updates their status.
- Persistently store tasks in a text file for future access.

## License

This project is open-source and available for modification and distribution.
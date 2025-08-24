TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as f:
            for line in f:
                desc, status = line.strip().rsplit(" | ", 1)
                tasks.append({"desc": desc, "completed": status == "completed"})
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            status = "completed" if task["completed"] else "pending"
            f.write(f"{task['desc']} | {status}\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. [{status}] {task['desc']}")

def add_task(tasks):
    desc = input("Enter task description: ").strip()
    if desc:
        tasks.append({"desc": desc, "completed": False})
        save_tasks(tasks)
        print("Task added.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: "))
        if 1 <= idx <= len(tasks):
            tasks.pop(idx - 1)
            save_tasks(tasks)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed(tasks):
    display_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as completed: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Manager")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
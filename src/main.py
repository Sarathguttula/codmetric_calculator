# filepath: todo-list-manager/src/main.py

from task_manager import TaskManager

def main():
    task_manager = TaskManager()
    task_manager.load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == '2':
            task_id = int(input("Enter the task ID to delete: "))
            task_manager.delete_task(task_id)
        elif choice == '3':
            task_manager.display_tasks()
        elif choice == '4':
            task_id = int(input("Enter the task ID to mark as completed: "))
            task_manager.mark_completed(task_id)
        elif choice == '5':
            task_manager.save_tasks()
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
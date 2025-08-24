def format_task_string(task):
    return f"[{'X' if task['completed'] else ' '}] {task['title']}"

def read_tasks_from_file(filepath):
    tasks = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                title, completed = line.strip().rsplit(',', 1)
                tasks.append({'title': title, 'completed': completed == 'True'})
    except FileNotFoundError:
        pass
    return tasks

def write_tasks_to_file(filepath, tasks):
    with open(filepath, 'w') as file:
        for task in tasks:
            file.write(f"{task['title']},{task['completed']}\n")
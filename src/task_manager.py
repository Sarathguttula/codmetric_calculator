class TaskManager:
    def __init__(self, filename='tasks.txt'):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        self.save_tasks()

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()

    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            status = '✓' if task['completed'] else '✗'
            print(f"{index + 1}. [{status}] {task['task']}")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]['completed'] = True
            self.save_tasks()

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                line = f"{task['task']}|{task['completed']}\n"
                file.write(line)

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    task, completed = line.strip().split('|')
                    self.tasks.append({'task': task, 'completed': completed == 'True'})
        except FileNotFoundError:
            pass  # If the file doesn't exist, we start with an empty task list.
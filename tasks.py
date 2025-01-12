from dataclasses import dataclass


@dataclass
class Task:
    title: str
    is_complete: bool = False


class TaskModel:
    def __init__(self):
        self.tasks: list[Task] = list()
    
    def add_tasks(self, task_name: str):
        task = Task(title=task_name)
        self.tasks.append(task)
        print(f"{task.title} ajoutée.")
    
    def get_tasks(self):
        return self.tasks
    
    def update_complete(self, task: Task):
        while True:
            state: str = input("""
                            1: Compléter la tâche
                            2: Marquer comme incomplète
                            """)
            if state == "1":
                task.is_complete = True
                break
            elif state == "2":
                task.is_complete = False
                break
            else:
                print("Invalide")

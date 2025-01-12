from tasks import TaskModel, Task


class TaskView:
    def __init__(self, task_manager: TaskModel):
        self.task_manager = task_manager
    
    def display_tasks(self):
        for i, task in enumerate(self.task_manager.get_tasks()):
            button = "👌" if task.is_complete else "👎"
            print(f"""
                  {i} - {task.title} - {button}
                  """)
    
    def add_task(self):
        task_name = input("Quel est le nom de la tâche à créer ? ")
        self.task_manager.add_tasks(task_name)
    
    def update_task(self):
        task_index = input("Quel est l'index de la tâche à modifier ? ")
        try:
            task: Task = self.task_manager.get_tasks()[int(task_index)]
            task.is_complete = True if not task.is_complete else False
        
        except (IndexError, ValueError):
            print("Pas de tâches correspondante trouvée")

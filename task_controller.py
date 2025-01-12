from task_view import TaskView


class Controller:
    
    def __init__(self, task_view: TaskView):
        self.view = task_view
        self.actions_mapping = {"1": self.view.add_task,
                                "2": self.view.display_tasks,
                                "3": self.view.update_task}
    
    def run(self):
        while True:
            choice = input("""
                           1. Ajouter une tâche ?
                           2. Afficher les tâches ?
                           3. Mettre à jour les tâches ?
                           4. Quitter le programme ?
                           """)
            
            if choice == "4":
                break
        
            action = self.actions_mapping.get(choice)
            if action:
                action()
            else:
                print("Mauvais choix")
    
from task_controller import Controller
from task_view import TaskView
from tasks import TaskModel


if __name__ == "__main__":
    model = TaskModel()
    view = TaskView(model)
    controller = Controller(view)
    controller.run()

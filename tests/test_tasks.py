import pytest
from tasks import Task, TaskModel


def test_task_is_added():
    # Plutôt créer des fixtures pour ça :) A vous de jouer !
    task_model = TaskModel()
    task_model.add_tasks("Ajouter des tests")
    assert len(task_model.get_tasks()) == 1

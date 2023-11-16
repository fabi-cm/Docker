from abc import ABC, abstractmethod
from .models import Task

class TaskRepository(ABC):
    @abstractmethod
    def create_task(self, title, description):
        pass

    @abstractmethod
    def get_task_by_id(self, task_id):
        pass

    @abstractmethod
    def mark_task_as_completed(self, task_id):
        pass

class DjangoTaskRepository(TaskRepository):
    def create_task(self, title, description):
        return Task.objects.create(title=title, description=description)

    def get_task_by_id(self, task_id):
        return Task.objects.get(pk=task_id)

    def mark_task_as_completed(self, task_id):
        task = Task.objects.get(pk=task_id)
        task.completed = True
        task.save()
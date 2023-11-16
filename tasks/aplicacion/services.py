from ..dominio.repositories import TaskRepository

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, title, description):
        return self.task_repository.create_task(title, description)

    def get_task_by_id(self, task_id):
        return self.task_repository.get_task_by_id(task_id)

    def mark_task_as_completed(self, task_id):
        return self.task_repository.mark_task_as_completed(task_id)

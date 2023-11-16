from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from ..aplicacion.services import TaskService
from ..dominio.models import Task

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = TaskService().create_task(title, description)
        return redirect('task_detail', task_id=task.id)
    return render(request, 'tasks/create_task.html')

def task_detail(request, task_id):
    try:
        task = TaskService().get_task_by_id(task_id)
        return render(request, 'tasks/task_detail.html', {'task': task})
    except task.DoesNotExist:
        return HttpResponseNotFound("Task not found")

def mark_task_as_completed(request, task_id):
    TaskService().mark_task_as_completed(task_id)
    return redirect('task_detail', task_id=task_id)

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
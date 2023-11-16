from django.urls import path
from .infraestructura import views
from .aplicacion.services import TaskService    

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete/', views.mark_task_as_completed, name='mark_task_as_completed'),
]
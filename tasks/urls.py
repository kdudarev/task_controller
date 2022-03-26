from django.urls import path

from .views import HomeView, TaskDetailView, AddTaskView


app_name = 'tasks'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
]

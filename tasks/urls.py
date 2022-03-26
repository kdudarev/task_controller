from django.urls import path

from .views import HomeView, TaskDetailView, AddTaskView, EditTaskView, \
    DeleteTaskView

app_name = 'tasks'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('add_task/', AddTaskView.as_view(), name='add_task'),
    path('edit_task/<int:pk>/', EditTaskView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>/', DeleteTaskView.as_view(),
         name='delete_task'),
]

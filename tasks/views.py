from django.views.generic import ListView, DetailView

from tasks.models import Task


class HomeView(ListView):
    model = Task
    template_name = 'tasks/home.html'
    ordering = ['-date_added']


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

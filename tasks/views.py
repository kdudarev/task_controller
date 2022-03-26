from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView

from .forms import TaskForm, EditTaskForm
from .models import Task


class HomeView(ListView):
    model = Task
    template_name = 'tasks/home.html'
    ordering = ['-date_added']


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'


class AddTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add_task.html'

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super(AddTaskView, self).form_valid(form)


class EditTaskView(UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'tasks/edit_task.html'


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_url = reverse_lazy('tasks:home')

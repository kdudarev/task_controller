from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'text', 'assignee', 'deadline', 'status', 'priority')


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'text', 'assignee', 'deadline', 'status', 'priority')

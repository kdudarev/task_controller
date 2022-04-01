from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True,
                                    upload_to='images/profile/')
    github_url = models.CharField(max_length=255, null=True, blank=True)
    telegram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = 'Profiles'
        verbose_name = 'Profile'
        ordering = ['user']


class Task(models.Model):
    STATUSES = (
        ('to-do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('testing', 'Testing'),
        ('done', 'Done')
    )
    PRIORITIES = (
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('high', 'High'),
        ('highest', 'Highest')
    )
    name = models.CharField(max_length=50, verbose_name='Task')
    text = models.TextField(null=True, blank=True, verbose_name='Description')
    date_added = models.DateField(auto_now_add=True, verbose_name='Date added')
    reporter = models.ForeignKey(User, related_name='reporter',
                                 on_delete=models.SET('isDeleted'),
                                 verbose_name='Reporter')
    assignee = models.ForeignKey(User, related_name='assignee',
                                 on_delete=models.SET('isDeleted'),
                                 verbose_name='Assignee')
    deadline = models.DateField(null=True, blank=True, verbose_name='Deadline')
    status = models.CharField(max_length=15, choices=STATUSES, default='to-do',
                              verbose_name='Status')
    priority = models.CharField(max_length=10, choices=PRIORITIES,
                                default='normal', verbose_name='Priority')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks:task_detail', args=[self.pk])

    class Meta:
        verbose_name_plural = 'Tasks'
        verbose_name = 'Task'
        ordering = ['-date_added']

from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    name = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.name

class TodoItem(models.Model):
    name = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete = models.CASCADE)

    # optional fields for weather api idea.
    date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
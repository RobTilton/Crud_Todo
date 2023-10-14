from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    owned_tables = models.ManyToManyField('TodoList', related_name='owners')

    def __str__(self):
        return self.user.username

class TodoList(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    tableNumber = models.AutoField(primary_key=True, unique=True)  # `tableNumber` is PKey.
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} (List number {self.tableNumber})"

class TodoItem(models.Model):
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    DoByDate = models.DateTimeField(null=True, blank=True)
    Location = models.CharField(max_length=255, blank=True)
    Needs = models.TextField(blank=True)
    Additional = models.TextField(blank=True)

    def __str(self):
        return self.name


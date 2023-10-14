from django.contrib import admin
from .models import UserProfile, TodoList, TodoItem

admin.site.register(UserProfile)
admin.site.register(TodoList)
admin.site.register(TodoItem)
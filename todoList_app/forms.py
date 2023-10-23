from django import forms
from .models import TodoList, TodoItem

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['name']

class TodoListItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['name', 'completed', 'date', 'address']
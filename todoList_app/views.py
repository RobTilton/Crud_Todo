from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TodoList, TodoItem
from .forms import TodoListForm


@login_required
def Home(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            new_list.save()
            return redirect('home')
    else:
        form = TodoListForm()
    
    user_lists = TodoList.objects.filter(user=request.user)
    
    return render(request, 'home.html', {'user_lists': user_lists, 'form': form})




@login_required
def View_Todo_List(request, todo_list_id):
    user_lists = TodoList.objects.filter(user=request.user)
    try:
        todo_list = TodoList.objects.get(pk=todo_list_id)
        todo_items = TodoItem.objects.filter(todo_list=todo_list)
    except TodoList.DoesNotExist:
        todo_list = None
        todo_items = []
    
    return render(request, 'home.html', {'user_lists': user_lists, 'selected_todo_list': todo_list, 'todo_items': todo_items, 'form': TodoListForm()})
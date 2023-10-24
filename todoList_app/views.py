from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.http import HttpResponseNotFound
from .models import TodoList, TodoItem
from .forms import TodoListForm, TodoListItemForm


def Handle_Todo_List_Creation(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_list = form.save(commit=False)
        new_list.user = request.user
        new_list.save()
        request.session['selected_todo_list_id'] = new_list.id
        return redirect('view_todo_list', todo_list_id=new_list.id)
    return redirect('home')


@login_required
def Home(request):
    if request.method == 'POST':
        return Handle_Todo_List_Creation(request)
    else:
        form = TodoListForm()
        user_lists = TodoList.objects.filter(user=request.user)
        
        selected_todo_list_id = request.session.get('selected_todo_list_id')
        selected_todo_list = TodoList.objects.filter(user=request.user, id=selected_todo_list_id).first()
    return render(request, 'home.html', {'user_lists': user_lists, 'form': form, 'selected_todo_list': selected_todo_list})
    
    

def Handle_Delete_List(request, todo_list):
    todo_list.delete()
    return redirect('home')

def Handle_Item_Creation(request, todo_list):
    item_form = TodoListItemForm(request.POST)
    if item_form.is_valid():
        new_item = item_form.save(commit=False)
        new_item.todo_list = todo_list
        new_item.save()
        return redirect('home.html')



@login_required
def View_Todo_List(request, todo_list_id):
    user_lists = TodoList.objects.filter(user=request.user)
    item_form = TodoListItemForm()
    try:
        todo_list = TodoList.objects.get(pk=todo_list_id)
        request.session['selected_todo_list_id'] = todo_list.id
    except TodoList.DoesNotExist:
        return HttpResponseNotFound('Todo list not found')

    todo_items = TodoItem.objects.filter(todo_list=todo_list)
    
    if request.method == 'POST' and 'add_item' in request.POST:
        Handle_Item_Creation(request, todo_list)

    if request.method == 'POST' and 'delete_list' in request.POST:
        return Handle_Delete_List(request, todo_list)
    
    return render(request, 'home.html', {'user_lists': user_lists, 'selected_todo_list': todo_list, 'todo_items': todo_items, 'form': TodoListForm(), 'item_form': item_form})


def edit_todo_item(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    form = TodoListItemForm(instance=item)
    if request.method == 'POST':
        form = TodoListItemForm(request.POST, instance=item)
        if 'update_item' in request.POST:
            if form.is_valid():
                form.save()
            return redirect('home')

        elif 'delete_item' in request.POST:
            item.delete()
            return redirect('home')
        
    return render(request, 'edit_todo_item.html', {'form': form})
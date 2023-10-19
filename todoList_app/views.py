from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TodoList
from .forms import TodoListForm


@login_required
def Home(request):
    user_lists = TodoList.objects.filter(user=request.user)
    return render(request, 'home.html', {'user_lists': user_lists})


@login_required
def ListCreation(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            new_list.save()
            return redirect('home')
    else:
        form = TodoListForm()
    return render(request, 'new_list.html', {'form': form})


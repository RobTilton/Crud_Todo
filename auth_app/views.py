from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from . import models

def Home(request):
    return render(request, 'home.html')

def Login(request):
    return render(request, 'login.html')
    

def Logout(request):
    return render(request, 'logout.html')


def Registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request , 'registration.html', {'form': form})
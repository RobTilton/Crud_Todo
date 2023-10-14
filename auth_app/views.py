from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . import models


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


def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                return redirect('home')
    
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

    

def Logout(request):
    logout(request)
    return redirect('login')
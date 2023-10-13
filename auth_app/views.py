from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

def Home(request):
    return render(request, 'home.html')

def Login(request):
    return render(request, 'login.html')
    

def Logout(request):
    return render(request, 'logout.html')


def Registration(request):
    return render(request , 'registration.html')
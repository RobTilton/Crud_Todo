from django.shortcuts import render
from . import models
# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Login(request):
    return render(request, 'login.html')

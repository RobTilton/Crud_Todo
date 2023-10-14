from django.shortcuts import render, redirect
from . import models

def Home(request):
    return render(request, 'home.html')




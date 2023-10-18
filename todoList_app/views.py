from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models


@login_required
def Home(request):
    return render(request, 'home.html')


@login_required
def ListCreation(request):
    return render(request, 'new_list.html')


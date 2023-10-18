from django.urls import path
from . import views



urlpatterns = [
    path('home/', views.Home, name='home'),
    path('new_list/', views.ListCreation, name='new_list'),
]
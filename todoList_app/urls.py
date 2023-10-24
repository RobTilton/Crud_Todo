from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('view_todo_list/<int:todo_list_id>/', views.View_Todo_List, name='view_todo_list'),
    path('edit_todo_item/<int:item_id>/', views.edit_todo_item, name='edit_todo_item'),
]
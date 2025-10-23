from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.task_list, name='list'),
    path('create/', views.task_create, name='create'),
    path('update/<int:pk>/', views.task_update, name='update'),
    path('delete/<int:pk>/', views.task_delete, name='delete'),
]


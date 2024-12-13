from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.task_add, name='task_add'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/edit/', views.edit_task, name='task_edit'),
    path('<int:pk>/delete/', views.delete_task, name='task_delete'),
]

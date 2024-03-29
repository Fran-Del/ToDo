from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<str:pk>/', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>/', views.deleteTask, name='delete'),
]
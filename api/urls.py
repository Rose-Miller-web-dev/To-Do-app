from django.urls import path
from . import views

urlpatterns = [
    path('rest_framework_get_tasks/', views.get_tasks, name="drf_get_tasks"),
    path('rest_framework_get_task_detail/<str:pk>/', views.get_task_detail, name="drf_get_task_detail"),
    path('rest_framework_create_task/', views.create_task, name="drf_create_task"),
    path('rest_framework_update_task/<str:pk>/', views.update_task, name="drf_update_task"),
    path('rest_framework_delete_task/<str:pk>/', views.delete_task, name="drf_delete_task")
]
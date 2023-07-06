from django.urls import path
from . import views

urlpatterns = [
    path('rest_framework_get_tasks/', views.get_tasks, name="drf_get_tasks"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name="lp"),
    path('task_list/', views.task_list, name="task_list"),
    path('tasks/<str:pk>/', views.task_detail, name="task_detail"),
    path('create_task/', views.create_task, name="create_task"),
    path('update_task/<str:pk>/', views.update_task, name="update_task"),
    path('delete_task/<str:pk>/', views.delete_task, name="delete_task"),
    path('login_user/', views.login_user, name="login_user"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('register_user/', views.register_user, name="register_user"),
]
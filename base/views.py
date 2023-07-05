from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from .models import Task
from .forms import TaskForm
# Create your views here.

def landing_page(request):
    context = {}
    return render(request, 'base/lp.html', context)

def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'base/task_list.html', context)

def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    context = { 'task': task }
    return render(request, 'base/task_detail.html', context)

def create_task(request):
    task_form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            return redirect('task_list')

    context = { 'form': task_form }
    return render(request, 'base/create_task.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    context = { 'form': form }
    return render(request, 'base/create_task.html', context)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')

    context = {'task': task}
    return render(request, 'base/delete_task.html', context)

def login_user(request):
    page = 'login'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            messages.error(request, 'no user found bitch!')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)
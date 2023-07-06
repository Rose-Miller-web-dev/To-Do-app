from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.serializers import serialize
import json

from .serializer import TaskSerializer
from base.models import Task
# Create your views here.

@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()

    # serialized_data = serialize('json', tasks)
    # serialized_data = json.loads(serialized_data)

    serialized_data = TaskSerializer(tasks, many=True)
    return Response(serialized_data.data)

@api_view(['GET'])
def get_task_detail(request, pk):
    task = Task.objects.get(id=pk)
    serialized_data = TaskSerializer(task, many=False)
    return Response(serialized_data.data)

@api_view(['POST'])
def create_task(request):
    serialized_data = TaskSerializer(data=request.data)

    if serialized_data.is_valid():
        serialized_data.save()

    return Response(serialized_data.data)

@api_view(['POST'])
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    
    task.delete()

    return redirect('drf_get_tasks')
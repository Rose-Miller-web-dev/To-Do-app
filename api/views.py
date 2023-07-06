from django.shortcuts import render
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

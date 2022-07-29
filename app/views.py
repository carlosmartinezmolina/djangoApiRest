from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializers
from rest_framework import status
from django.http import Http404
from .models import Task
from django.core import serializers
    
class TestApi(APIView):

    def get(self, request, format=None, *args, **kwargs):
        task_list = list(Task.objects.all())
        task_list = [item.task for item in task_list]
        return Response(task_list)
        
    def post(self, request, format=None):
        queryset = Task.objects.filter(taskId=request.data['id'])
        if(not queryset):
            Task.objects.create(task=request.data['string'],taskId=request.data['id'])
        else:
            task = queryset.get()
            task.task = request.data['string']
            task.save() 
        return Response("task created" if not queryset else "task updated")
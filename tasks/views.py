# Create your views here.
# from django.http import JsonResponse
# from django.core.serializers import serialize
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

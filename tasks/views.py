# Create your views here.
# from django.http import JsonResponse
# from django.core.serializers import serialize
from .models import Task
from rest_framework import viewsets,status
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['priority']

    def get_queryset(self):
        return self.request.user.tasks.all()
    '''
    def create(self, request, *args, **kwargs):
        data = request.data
        data["user"] = self.request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    '''
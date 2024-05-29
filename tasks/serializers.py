from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    '''
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )
    '''

    class Meta:
        model = Task
        fields = ["name", "description", "priority","user", "completed"]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(TaskSerializer,self).create(validated_data)        


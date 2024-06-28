from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["name", "description", "priority", "user"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super(TaskSerializer, self).create(validated_data)


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id", "name", "description","priority", "completed"]


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["name", "description", "priority","completed"]

    def update(self, instance, validated_data):
        validated_data["user"] = self.context["request"].user
        return super(TaskUpdateSerializer, self).update(instance, validated_data)

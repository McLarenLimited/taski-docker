"""Serializers for the API application."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model.

    Provides serialization/deserialization of Task instances.
    """

    class Meta:
        """Meta class for TaskSerializer configuration."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')

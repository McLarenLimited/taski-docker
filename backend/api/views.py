"""Views for the API application."""
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """ViewSet for handling Task model operations.

    Provides CRUD operations for Task model using ModelViewSet.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """Return serialized data of deleted task with HTTP 200 status.

        Overrides default destroy() to return instead of HTTP 204.
        """
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)

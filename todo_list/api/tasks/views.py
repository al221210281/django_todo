from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo_list.core import models as core_models
from todo_list.api.tasks import serializers as tasks_serializers


class TaskViewSet(viewsets.ModelViewSet):
    """
    API para CRUD de Tasks

    """
    serializer_class = tasks_serializers.TaskSerializer
    queryset = core_models.Task.objects.all()

    def get_permissions(self):
        """

        """
        if self.action == 'list':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

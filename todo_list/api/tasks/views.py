from rest_framework import viewsets

from todo_list.core import models as core_models
from todo_list.api.tasks import serializers as tasks_serializers


class TaskViewSet(viewsets.ModelViewSet):
    """
    API para CRUD de Tasks

    """
    serializer_class = tasks_serializers.TaskSerializer
    queryset = core_models.Task.objects.all()

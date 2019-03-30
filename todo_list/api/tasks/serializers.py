from rest_framework import serializers

from todo_list.core import models as core_models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = core_models.Task
        fields = (
            'id',
            'description',
            'status',
        )

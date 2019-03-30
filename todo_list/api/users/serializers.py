from rest_framework import serializers

from todo_list.users import models as users_models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users_models.User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
        )

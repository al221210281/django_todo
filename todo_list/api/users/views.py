from rest_framework import viewsets

from todo_list.api.users import serializers as users_serializers
from todo_list.users import models as users_models


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API para Users

    """
    serializer_class = users_serializers.UserSerializer
    queryset = users_models.User.objects.filter(is_active=True)

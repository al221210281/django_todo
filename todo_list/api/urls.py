from rest_framework import routers

from todo_list.api.tasks import views as tasks_views
from todo_list.api.users import views as users_views


router = routers.SimpleRouter()
router.register(r'tasks', tasks_views.TaskViewSet)
router.register(r'users', users_views.UserViewSet)

urlpatterns = [

]

urlpatterns += router.urls

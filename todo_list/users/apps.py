from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "todo_list.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass

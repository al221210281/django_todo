from django.contrib import admin

from todo_list.core import models as core_models


@admin.register(core_models.Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Define el comportamiento del modelo en el Admin

    """
    list_display = ["description", "status", ]
    search_fields = ["description", ]
    ordering = ["status", ]

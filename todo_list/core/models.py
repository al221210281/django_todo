from django.db import models


class Task(models.Model):
    """
    Modelo de tareas

    """
    description = models.CharField(max_length=255, blank=False, null=False)
    status = models.BooleanField(blank=True, default=False)

    def __str__(self):
        """
        convierte el objeto a String

        """
        status = 'completada' if self.status else 'pendiente'
        return f'Tarea: {self.description} {status}'


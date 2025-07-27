"""Models for the API application."""
from django.db import models


class Task(models.Model):
    """Task model representing a single task item."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Return string representation of the Task model."""
        return self.title

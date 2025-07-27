"""Django app configuration for the API module."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration for the 'api' Django application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

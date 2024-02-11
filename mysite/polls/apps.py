"""Polls app config"""

from django.apps import AppConfig


class PollsConfig(AppConfig):
    """PollsConfig app config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"

"""
Module: course apps

This module defines the configuration class for the course app.
"""

from django.apps import AppConfig


class CourseConfig(AppConfig):
    """Configuration class for the course app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "course"

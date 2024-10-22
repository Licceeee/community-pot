"""
Module: course apps

This module contains the configuration for the course app.
"""

from django.apps import AppConfig


class CourseConfig(AppConfig):
    """Configuration for the course app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "course"

"""
Module: course urls

This module defines the URL patterns for the course app.
"""

from django.urls import path, include

urlpatterns = [
    path("ckeditor/", include("django_ckeditor_5.urls")),
]

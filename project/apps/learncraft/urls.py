"""
Module: course urls

This module defines the URL patterns for the course app.
"""

from django.urls import path, include

from .views import LearnCarftView

urlpatterns = [
    path("ironhack/", LearnCarftView.as_view(), name="learncraft-list"),
    path("ckeditor/", include("django_ckeditor_5.urls")),
]

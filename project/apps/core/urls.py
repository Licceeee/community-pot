"""
Module: core urls

This module defines the URL patterns for the core app.
"""

from django.urls import path

from .views import IndexView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

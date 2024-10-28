"""
Module: core urls

This module defines the URL patterns for the core app.
"""

from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import IndexView


urlpatterns = [
    path("", login_required(IndexView.as_view()), name="index"),
]

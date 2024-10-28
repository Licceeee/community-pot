"""
Module: user apps

This module defines the configuration for the user app.
"""

from django.db import models


class Timestamps(models.Model):
    """Abstract model with timestamps."""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class for the Timestamps model."""

        abstract = True

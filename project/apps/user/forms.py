"""
Module: user forms

This module defines the forms for the user app.
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Form for creating a new user."""

    class Meta:
        """Meta class for the CustomUserCreationForm."""

        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    """Form for changing a user."""

    class Meta:
        """Meta class for the CustomUserChangeForm."""

        model = CustomUser
        fields = ("email",)
